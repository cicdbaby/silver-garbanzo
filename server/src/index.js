// Menzil · Gök — room server.
// The server is referee and postman, not the game: it pairs two players under a room code, keeps the clock,
// and every 100 ms hands both of them the same "turn" — the list of orders given in that window, each stamped
// with the side that sent it. Both browsers run the same deterministic match from the same seed and orders.
// It also compares the state fingerprints both clients report, so a desync is caught instead of silently diverging.

const TURN_MS = 100;          // one turn = 6 sim ticks of 1/60 s
const TICKS_PER_TURN = 6;
const GRACE_MS = 90_000;      // how long a dropped player may take to come back
const MAX_MSG = 16_000;       // bytes
const CMD_KINDS = new Set(['build', 'buy', 'launch', 'sortie', 'engage', 'sat', 'go', 'mode', 'emit', 'sell', 'rebuild']);
const NATS = new Set(['TR', 'US', 'RU', 'CN', 'IL']);
const CODE_RE = /^[A-Z2-9]{5}$/;

const cors = r => { r.headers.set('Access-Control-Allow-Origin', '*'); return r };
const json = (o, status = 200) => cors(new Response(JSON.stringify(o), { status, headers: { 'content-type': 'application/json' } }));

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (url.pathname === '/health') return json({ ok: true, service: 'menzil-oda' });
    const m = url.pathname.match(/^\/room\/([A-Za-z0-9]+)$/);
    if (m) {
      const code = m[1].toUpperCase();
      if (!CODE_RE.test(code)) return json({ error: 'bad code' }, 400);
      if (req.headers.get('Upgrade') !== 'websocket') return json({ error: 'websocket expected' }, 426);
      return env.ROOMS.get(env.ROOMS.idFromName(code)).fetch(req);
    }
    // everything else is the game itself (static files built into dist/)
    if (env.ASSETS) return env.ASSETS.fetch(req);
    return json({ error: 'not found' }, 404);
  }
};

export class Room {
  constructor(state, env) {
    this.state = state;
    this.players = [];        // {side, tok, nat, ws, on, goneAt, cmdT, cmdN}
    this.phase = 'lobby';     // lobby | play | over
    this.opts = null;
    this.n = 0;               // last turn sent
    this.queue = [];          // [side, kind, args] for the next turn
    this.hist = [];           // [turn, cmds] for every turn that carried orders
    this.hashes = new Map();  // tick -> {side: hash}
    this.timer = null;
  }

  async fetch(req) {
    const url = new URL(req.url);
    const pair = new WebSocketPair();
    const [client, server] = Object.values(pair);
    server.accept();
    const tok = (url.searchParams.get('tok') || '').slice(0, 40);
    server.addEventListener('message', e => this.onMsg(server, e.data));
    server.addEventListener('close', () => this.onClose(server));
    server.addEventListener('error', () => this.onClose(server));
    server.tok = tok;
    return new Response(null, { status: 101, webSocket: client });
  }

  send(ws, o) { try { ws.send(JSON.stringify(o)) } catch (e) { } }
  all(o) { const s = JSON.stringify(o); for (const p of this.players) if (p.on) try { p.ws.send(s) } catch (e) { } }
  me(ws) { return this.players.find(p => p.ws === ws) }
  lobbyView() { return this.players.map(p => ({ side: p.side, nat: p.nat, on: p.on })) }
  lobbyCast() { const players = this.lobbyView(); for (const p of this.players) if (p.on) this.send(p.ws, { t: 'lobby', side: p.side, players }) }

  onMsg(ws, data) {
    if (typeof data !== 'string' || data.length > MAX_MSG) return;
    let m; try { m = JSON.parse(data) } catch (e) { return }
    if (m.t === 'ping') return this.send(ws, { t: 'pong', at: m.at });
    if (m.t === 'hello') return this.hello(ws, m);
    const p = this.me(ws); if (!p) return;
    if (m.t === 'nat' && this.phase === 'lobby') {
      if (!NATS.has(m.nat) || this.players.some(q => q !== p && q.nat === m.nat)) return this.send(ws, { t: 'err', m: 'Bu ülke rakipte.' });
      p.nat = m.nat; return this.lobbyCast();
    }
    if (m.t === 'start' && this.phase === 'lobby' && p.side === 'W') return this.start();
    if (m.t === 'cmd' && this.phase === 'play') {
      if (!CMD_KINDS.has(m.k) || !Array.isArray(m.a)) return;
      const now = Date.now(); if (now - (p.cmdT || 0) > 1000) { p.cmdT = now; p.cmdN = 0 }
      if (++p.cmdN > 40) return;                       // flood guard
      this.queue.push([p.side, m.k, m.a]); return;
    }
    if (m.t === 'hash' && this.phase === 'play') return this.hash(p, m.tick | 0, String(m.h).slice(0, 16));
    if (m.t === 'over' && this.phase === 'play') { this.phase = 'over'; this.stop(); return this.all({ t: 'over' }) }
  }

  hello(ws, m) {
    // reconnect: same token takes its seat back
    let p = this.players.find(q => q.tok && q.tok === ws.tok);
    if (p) {
      if (p.ws && p.ws !== ws) try { p.ws.close(4000, 'replaced') } catch (e) { }
      p.ws = ws; p.on = true; p.goneAt = 0;
    } else {
      if (this.players.length >= 2 || this.phase !== 'lobby') { this.send(ws, { t: 'err', m: this.phase === 'lobby' ? 'Oda dolu.' : 'Bu odada maç başladı.' }); try { ws.close(4001, 'full') } catch (e) { } return }
      const side = this.players.some(q => q.side === 'W') ? 'E' : 'W';
      let nat = NATS.has(m.nat) ? m.nat : 'TR';
      if (this.players.some(q => q.nat === nat)) nat = [...NATS].find(k => !this.players.some(q => q.nat === k));
      p = { side, tok: ws.tok || crypto.randomUUID(), nat, ws, on: true, goneAt: 0 };
      this.players.push(p);
    }
    this.send(ws, { t: 'welcome', side: p.side, tok: p.tok, phase: this.phase, players: this.lobbyView() });
    if (this.phase === 'lobby') this.lobbyCast();
    else {
      // back into a running match: everything needed to rebuild it locally
      this.send(ws, { t: 'sync', opts: this.opts, n: this.n, hist: this.hist, tt: TICKS_PER_TURN });
      this.all({ t: 'peer', side: p.side, on: true });
      if (this.phase === 'play' && !this.timer && this.players.every(q => q.on)) this.run();
    }
  }

  start() {
    if (this.players.length !== 2 || !this.players.every(p => p.on)) return;
    const W = this.players.find(p => p.side === 'W'), E = this.players.find(p => p.side === 'E');
    const seed = crypto.getRandomValues(new Uint32Array(1))[0];
    this.opts = { mode: 'war', m: 'war', nat: W.nat, enat: E.nat, enatSel: E.nat, diff: 'hard', seed, hum: { W: 1, E: 1 }, online: 1, designs: [] };
    this.phase = 'play'; this.n = 0; this.queue = []; this.hist = []; this.hashes.clear();
    this.all({ t: 'start', opts: this.opts, tt: TICKS_PER_TURN });
    this.run();
  }

  run() {
    if (this.timer) return;
    this.timer = setInterval(() => this.tick(), TURN_MS);
  }
  stop() { if (this.timer) { clearInterval(this.timer); this.timer = null } }

  tick() {
    if (this.phase !== 'play') return this.stop();
    const now = Date.now();
    const gone = this.players.find(p => !p.on);
    if (gone) {
      // hold the clock while someone is away, so nobody plays against a frozen opponent
      if (now - gone.goneAt > GRACE_MS) { this.phase = 'over'; this.stop(); this.all({ t: 'abandon', side: gone.side }) }
      return;
    }
    this.n++;
    const c = this.queue; this.queue = [];
    if (c.length) this.hist.push([this.n, c]);
    this.all({ t: 'turn', n: this.n, c });
  }

  hash(p, tick, h) {
    let rec = this.hashes.get(tick);
    if (!rec) { rec = {}; this.hashes.set(tick, rec) }
    rec[p.side] = h;
    if (rec.W && rec.E) {
      this.hashes.delete(tick);
      if (rec.W !== rec.E) { this.all({ t: 'desync', tick }); this.phase = 'over'; this.stop() }
    }
    if (this.hashes.size > 120) { const old = [...this.hashes.keys()].sort((a, b) => a - b).slice(0, 60); for (const k of old) this.hashes.delete(k) }
  }

  onClose(ws) {
    const p = this.me(ws); if (!p) return;
    p.on = false; p.goneAt = Date.now(); p.ws = null;
    if (this.phase === 'lobby') {
      this.players = this.players.filter(q => q !== p);
      // the guest becomes host if the host leaves before the start
      if (this.players.length === 1) this.players[0].side = 'W';
      this.lobbyCast();
    } else if (this.phase === 'play') this.all({ t: 'peer', side: p.side, on: false });
    if (!this.players.some(q => q.on)) this.stop();
  }
}

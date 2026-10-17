# Two-player online test: run `npx wrangler dev --port 8787` in server/, `npm run build`, then
#   python3 tools/duel_test.py <port> [seconds]   (needs srv.py helper from replay_test.py next to it)
import sys,json,random,time;sys.path.insert(0,".");from srv import serve
PORT=int(sys.argv[1]);DUR=int(sys.argv[2]) if len(sys.argv)>2 else 60;serve(port=PORT)
from playwright.sync_api import sync_playwright
NET='ws://127.0.0.1:8787'
ACT=r"""(seed)=>{const g=window.__gok,G=g.G,me=g.ME;if(!G||G.over)return 'x';let r=seed;const vr=()=>{r=(r*16807)%2147483647;return r/2147483647};
  const a=vr();
  if(G.phase==='prep'&&a<.5){const SITES=['LRAD','MRAD','CIWS','RAD','TEL','DLN','SHORAD'];const t=SITES[(vr()*SITES.length)|0];const p=g.advSpot(t,null);if(p)g.issue('build',me,t,p.x,p.y);return 'build '+t}
  if(G.phase==='prep'){g.issue('go');return 'go'}
  if(a<.3){const SITES=['LRAD','MRAD','CIWS','TEL','DLN'];const t=SITES[(vr()*SITES.length)|0];const p=g.advSpot(t,null);if(p)g.issue('build',me,t,p.x,p.y);return 'build'}
  if(a<.8){const e=G.ents.filter(e=>e.alive&&e.side!==me&&e.cat==='asset');const t=e[(vr()*e.length)|0];if(t){const k=['BM','CM','DRN'][(vr()*3)|0];g.issue('buy',me,k,2);g.issue('launch',me,k,2,t.x,t.y,[])}return 'launch'}
  const s=G.ents.filter(e=>e.alive&&e.side===me&&e.cat==='site');if(s.length)g.issue('mode',[s[(vr()*s.length)|0].id],['auto','sel'][(vr()*2)|0]);return 'mode'}"""
with sync_playwright() as p:
    b=p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
    A=b.new_context(viewport={'width':1100,'height':700}).new_page();B=b.new_context(viewport={'width':1100,'height':700}).new_page()
    errs=[];A.on('pageerror',lambda e:errs.append('A '+str(e)+(e.stack or '')[:300]));B.on('pageerror',lambda e:errs.append('B '+str(e)+(e.stack or '')[:300]))
    A.goto(f'http://localhost:{PORT}/?net={NET}');B.goto(f'http://localhost:{PORT}/?net={NET}');A.wait_for_timeout(4000)
    A.click('#ov [data-o="online"]');A.wait_for_timeout(300);A.click('#ov [data-lnat="US"]');A.click('#ov [data-o="lhost"]');A.wait_for_timeout(1500)
    code=A.evaluate("()=>window.__gok.NET&&window.__gok.NET.code");print('code',code,A.evaluate("()=>window.__gok.NET.phase"))
    B.click('#ov [data-o="online"]');B.wait_for_timeout(300);B.fill('#lcode',code);B.click('#ov [data-o="ljoin"]');B.wait_for_timeout(1500)
    print('B lobby',B.evaluate("()=>[window.__gok.NET.phase,window.__gok.NET.side,JSON.stringify(window.__gok.NET.players)]"))
    A.screenshot(path='duel_lobbyA.png');B.screenshot(path='duel_lobbyB.png')
    A.click('#ov [data-o="lstart"]');A.wait_for_timeout(3000)
    print('started',A.evaluate("()=>[window.__gok.ME,!!window.__gok.G&&window.__gok.G.tick]"),B.evaluate("()=>[window.__gok.ME,!!window.__gok.G&&window.__gok.G.tick]"))
    t0=time.time();i=0
    while time.time()-t0<DUR:
        for P,nm in ((A,'A'),(B,'B')):
            try:P.evaluate(ACT,random.randint(1,10**6))
            except Exception as ex: errs.append(nm+' ACT '+str(ex)[:200])
        A.wait_for_timeout(700);i+=1
        if errs:break
    sa=A.evaluate("()=>{const G=window.__gok.G;return {tick:G.tick,phase:G.phase,hl:G.hlog,rec:G.rec.length,over:G.over,net:window.__gok.NET.n}}")
    sb=B.evaluate("()=>{const G=window.__gok.G;return {tick:G.tick,phase:G.phase,hl:G.hlog,rec:G.rec.length,over:G.over,net:window.__gok.NET.n}}")
    common={t:h for t,h in sa['hl']};ok=[(t,h==common.get(t)) for t,h in sb['hl'] if t in common]
    print('A',sa['tick'],sa['phase'],sa['rec'],sa['net'],'B',sb['tick'],sb['phase'],sb['rec'],sb['net'])
    print('hash compare',len(ok),'all equal' if ok and all(x for _,x in ok) else ok[-5:])
    print('desync overlay?',A.evaluate("()=>document.querySelector('#ov h1')&&document.querySelector('#ov').hidden===false?document.querySelector('#ov h1').textContent:''"))
    A.screenshot(path='duelA.png');B.screenshot(path='duelB.png')
    print(errs[:4]);b.close()

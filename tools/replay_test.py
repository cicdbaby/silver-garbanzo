# Determinism check: plays seeded matches with random player commands, replays each record
# (same page twice + a fresh page) and compares state hashes. Run after `npm run build`:
#   python3 tools/replay_test.py [port]
import threading,http.server,functools,socketserver
def serve(d='/home/claude/silver-garbanzo/dist',port=8765):
    H=functools.partial(http.server.SimpleHTTPRequestHandler,directory=d)
    H.log_message=lambda *a,**k:None
    socketserver.TCPServer.allow_reuse_address=True
    s=socketserver.ThreadingTCPServer(('127.0.0.1',port),H);threading.Thread(target=s.serve_forever,daemon=True).start();return s

import sys,json
PORT=int(sys.argv[1]) if len(sys.argv)>1 else 8811
serve(port=PORT)
from playwright.sync_api import sync_playwright
PLAY=r"""async([m,ticks,seed])=>{const g=window.__gok;g.startGame(m,{nat:'TR',diff:'hard',seed});await new Promise(res=>{const f=()=>{if(g.G&&document.getElementById('ov').hidden)res();else setTimeout(f,20)};f()});
 const G=g.G;g.issue('auto',true);let rr=1;const vr=()=>{rr=(rr*16807)%2147483647;return rr/2147483647};
 const SITES=['LRAD','MRAD','CIWS','RAD','TEL','DLN','SHORAD','UPPER'];
 for(let i=0;i<ticks&&!G.over;i++){g.update(g.STEP);
   if(i%97===13){const a=vr();
     if(a<.25){const t=SITES[(vr()*SITES.length)|0];const p=g.advSpot?g.advSpot(t,null):null;if(p)g.issue('build','W',t,p.x,p.y)}
     else if(a<.5&&G.phase==='war'){const e=G.ents.filter(e=>e.alive&&e.side!=='W'&&e.cat==='asset');const t=e[(vr()*e.length)|0];if(t){const k=['BM','CM','DRN'][(vr()*3)|0];if(!(G.stock.W[k]>=2))g.issue('buy','W',k,2);g.issue('launch','W',k,2,t.x,t.y,[])}}
     else if(a<.6){const s=G.ents.filter(e=>e.alive&&e.side==='W'&&e.cat==='site');if(s.length)g.issue('mode',[s[(vr()*s.length)|0].id],['auto','sel','off'][(vr()*3)|0])}
     else if(a<.65&&G.phase==='prep')g.issue('go');
     else if(a<.75&&G.phase==='war'){g.openCon('atk');const e=G.ents.find(e=>e.alive&&e.side!=='W'&&e.cat==='asset');if(e){G.con.tgt={x:e.x,y:e.y,lbl:'x'};G.con.w=['BM','CM','DRN'][(vr()*3)|0];g.setArm(true);g.doFire(true)}}
   }}
 return g.matchRecord()}"""
with sync_playwright() as p:
    b=p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
    pg=b.new_page(viewport={'width':1000,'height':700});errs=[];pg.on('pageerror',lambda e:errs.append(str(e)+(e.stack or '')[:300]))
    pg.goto(f'http://localhost:{PORT}/');pg.wait_for_timeout(4000)
    for m,T in [('war',60*60*9),('ffa',60*60*6)]:
        rec=pg.evaluate(PLAY,[m,T,12345])
        h1=pg.evaluate("(r)=>window.__gok.replayMatch(r)",rec)
        h2=pg.evaluate("(r)=>window.__gok.replayMatch(r)",rec)
        # fresh page replay
        pg2=b.new_page(viewport={'width':1000,'height':700});pg2.on('pageerror',lambda e:errs.append('P2 '+str(e)))
        pg2.goto(f'http://localhost:{PORT}/');pg2.wait_for_timeout(4000)
        h3=pg2.evaluate("(r)=>window.__gok.replayMatch(r)",rec);pg2.close()
        print(m,'ticks',rec['ticks'],'cmds',len(rec['cmds']),'orig',rec['hash'],'replay',h1,h2,h3,'OK' if rec['hash']==h1==h2==h3 else 'MISMATCH',errs[:3],flush=True)
        json.dump(rec,open(f'rec_{m}.json','w'))
    b.close()

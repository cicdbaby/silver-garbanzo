import sys;sys.path.insert(0,"/tmp/claude-0/-home-claude-silver-garbanzo/6c6bc46c-8355-5fbb-89b9-e5ff46dbf728/scratchpad");from srv import serve;serve()
import random
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
    pg=b.new_page(viewport={'width':1100,'height':700});errs=[];pg.on('pageerror',lambda e:errs.append(str(e)+' | '+(e.stack or '')[:400]))
    pg.route('**/fonts.googleapis.com/**',lambda r:r.abort())
    pg.goto('http://localhost:8765/');pg.wait_for_timeout(5000)
    for mode in ['ffa','war']:
        pg.evaluate("""async(m)=>{const g=window.__gok;g.startGame(m,{nat:'TR',diff:'hard'});await new Promise(res=>{const f=()=>{if(g.G&&document.getElementById('ov').hidden)res();else setTimeout(f,20)};f()});g.G.autoW=true}""",mode)
        for step in range(35):
            # advance the sim a bit, let real frames + UI run
            pg.evaluate("()=>{const g=window.__gok;for(let i=0;i<20*8;i++)g.update(1/20)}")
            pg.wait_for_timeout(350)
            # random player actions
            x=random.randint(60,800);y=random.randint(80,560)
            act=random.choice(['click','click','key','wheel','con'])
            try:
                if act=='click':pg.mouse.click(x,y)
                elif act=='key':pg.keyboard.press(random.choice(['v','c','h','a','Escape','v']))
                elif act=='wheel':pg.mouse.move(x,y);pg.mouse.wheel(0,random.choice([-400,400]))
                else:pg.evaluate("()=>{const g=window.__gok;g.openCon('atk');const G=g.G;const e=G.ents.find(e=>e.alive&&e.side!=='W'&&e.cat==='asset');if(e){G.con.tgt={x:e.x,y:e.y,lbl:'x'};G.con.w=['BM','CM','DRN','HGV'][Math.random()*4|0];g.setArm(true);g.doFire&&g.doFire()}}")
            except Exception as ex: errs.append('ACT '+str(ex)[:200])
            if errs:break
        st=pg.evaluate("()=>{const G=window.__gok.G;return {t:Math.round(G.time),over:G.over,out:G.out}}")
        print(mode,st,errs[:4],flush=True);errs.clear()
    b.close()

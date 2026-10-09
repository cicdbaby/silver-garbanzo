import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
S='/tmp/claude-0/-home-claude-silver-garbanzo/6c6bc46c-8355-5fbb-89b9-e5ff46dbf728/scratchpad/'
src=Image.open(S+'m4_merged.png').convert('RGB')
big=src
big.save('/home/claude/silver-garbanzo/public/img/m4.webp','WEBP',quality=88,method=6)
src.resize((768,768),Image.LANCZOS).save('/home/claude/silver-garbanzo/public/img/m4s.webp','WEBP',quality=82)
N=2048
im=np.asarray(src.resize((N,N),Image.LANCZOS)).astype(float)
r,g,b=im[...,0],im[...,1],im[...,2];lum=(r+g+b)/3;sat=im.max(2)-im.min(2)
water=((b>r*1.25)&(b>g*0.92)&(lum<170))|((b>r*1.35)&(g>r*1.15)&(b>g*0.85))
water=ndi.binary_opening(water,iterations=1)
lab,n=ndi.label(water);sz=ndi.sum(water,lab,range(1,n+1));keep=np.zeros(n+1,bool);keep[1:]=sz>=30;big_id=np.argmax(sz)+1
mb=ndi.mean(b/np.maximum(r,1),lab,range(1,n+1))
keep[1:]=(sz>=250)&(mb>1.45);keep[big_id]=True;water=ndi.binary_closing(keep[lab],iterations=1)
land=~water
forest=land&(g>=r*0.97)&(lum<95)
rock=land&(lum>95)&(r>=g*0.93)&(sat<60)
sm=lambda m,s=1.0: ndi.gaussian_filter(m.astype(float),s)
W=sm(water,.8);F=sm(forest,1.4)*(1-W);R=sm(rock,1.4)*(1-W)
Image.fromarray((np.clip(np.dstack([W,F,R]),0,1)*255).astype(np.uint8),'RGB').save('/home/claude/silver-garbanzo/public/img/mat4.webp','WEBP',quality=92)
vis=np.zeros(im.shape);vis[...]=(150,120,90);vis[forest]=(30,80,30);vis[rock]=(200,180,170);vis[water]=(20,40,120)
Image.fromarray(vis.astype(np.uint8)).resize((768,768)).save(S+'mat4vis.png')
lab,n=ndi.label(water);sz=ndi.sum(water,lab,range(1,n+1))
print('frac W F R',[round(float(m.mean()),3) for m in (water,forest,rock)],'largest water frac',round(sz.max()/water.size,3),'n',n)

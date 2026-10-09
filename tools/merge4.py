import cv2,numpy as np
from PIL import Image
U='/root/.claude/uploads/6c6bc46c-8355-5fbb-89b9-e5ff46dbf728/'
P={'m4a':'c8ca5fcf-image.png','m4c':'f7c04053-image.png','m4b':'05f0cc96-image.png','m4d':'bf4bf3d1-image.png'}
S='/tmp/claude-0/-home-claude-silver-garbanzo/6c6bc46c-8355-5fbb-89b9-e5ff46dbf728/scratchpad/'
src=np.asarray(Image.open('/mnt/user-data/uploads/Desktop/menzil-gorseller/m4.png').convert('RGB'));W=src.shape[1];c=round(W*.46)
N=3000;base=cv2.resize(src,(N,N),interpolation=cv2.INTER_LANCZOS4).astype(np.float32)
acc=np.zeros((N,N,3),np.float32);wsum=np.zeros((N,N),np.float32)
org={'m4a':(0,0),'m4b':(W-c,0),'m4c':(0,W-c),'m4d':(W-c,W-c)}
for k,f in P.items():
    pc=np.asarray(Image.open(U+f).convert('RGB')).astype(np.float32);ph,pw=pc.shape[:2]
    crop=src[org[k][1]:org[k][1]+c,org[k][0]:org[k][0]+c]
    # register piece -> crop at 512 res on blurred grayscale
    R=512
    a=cv2.GaussianBlur(cv2.cvtColor(cv2.resize(crop,(R,R),interpolation=cv2.INTER_AREA),cv2.COLOR_RGB2GRAY).astype(np.float32),(0,0),2)
    b=cv2.GaussianBlur(cv2.cvtColor(cv2.resize(pc.astype(np.uint8),(R,R),interpolation=cv2.INTER_AREA),cv2.COLOR_RGB2GRAY).astype(np.float32),(0,0),2)
    Wm=np.eye(2,3,dtype=np.float32)
    try:
        cc,Wm=cv2.findTransformECC(a,b,Wm,cv2.MOTION_AFFINE,(cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,300,1e-6),None,5)
    except Exception as e: cc=None;print('ecc fail',k,e)
    print(k,'cc',cc,Wm.round(3).tolist())
    # Wm maps crop(R) coords -> piece(R) coords. Build canvas -> piece map.
    s_cv=c/W*N/R   # canvas px per R px
    x0=org[k][0]/W*N;y0=org[k][1]/W*N
    # canvas (X,Y) -> crop R: u=(X-x0)/s_cv ; piece R: Wm@[u,v,1]; piece px: *pw/R
    A=np.vstack([Wm,[0,0,1]])
    T=np.array([[1/s_cv,0,-x0/s_cv],[0,1/s_cv,-y0/s_cv],[0,0,1]])
    Sc=np.diag([pw/R,ph/R,1])
    M=(Sc@A@T)[:2]
    warped=cv2.warpAffine(pc,M,(N,N),flags=cv2.INTER_LANCZOS4|cv2.WARP_INVERSE_MAP,borderMode=cv2.BORDER_CONSTANT,borderValue=0)
    valid=cv2.warpAffine(np.ones((ph,pw),np.float32),M,(N,N),flags=cv2.INTER_LINEAR|cv2.WARP_INVERSE_MAP,borderValue=0)
    # colour: pull piece statistics 60% toward the original crop
    reg=valid>.99;bw=base[reg];pw_=warped[reg]
    for ch in range(3):
        m1,s1=pw_[:,ch].mean(),pw_[:,ch].std()+1e-3;m0,s0=bw[:,ch].mean(),bw[:,ch].std()
        t=.6;warped[...,ch]=(warped[...,ch]-m1)*(s1+(s0-s1)*t)/s1+m1+(m0-m1)*t
    # feather toward inner edges (not the map border)
    d=cv2.distanceTransform((valid>.99).astype(np.uint8),cv2.DIST_L2,5)
    yy,xx=np.mgrid[0:N,0:N]
    dd=d.copy()
    # distances to map border are not feathered
    edge=np.minimum.reduce([xx,yy,N-1-xx,N-1-yy]).astype(np.float32)
    dd=np.where(edge<=d+2,9999,d)
    wgt=np.clip(dd/60,0,1)*(valid>.99)
    acc+=warped*wgt[...,None];wsum+=wgt
out=base*(1-np.clip(wsum,0,1))[...,None]+acc/np.maximum(wsum,1e-6)[...,None]*np.clip(wsum,0,1)[...,None]
out=np.clip(out,0,255).astype(np.uint8)
Image.fromarray(out).save(S+'m4_merged.png')
Image.fromarray(out).resize((1000,1000),Image.LANCZOS).save(S+'m4_merged_s.jpg',quality=88)

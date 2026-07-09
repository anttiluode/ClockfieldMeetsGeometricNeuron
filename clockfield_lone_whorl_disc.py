"""
clockfield_lone_whorl_disc.py
=============================
The topology-corrected memory test. Every earlier pinning experiment ran on a
periodic torus, where total winding is identically zero, so whorls come in +-
pairs that annihilate -- an artifact absent from the real systems (a cortical
patch and the Rajapinta box are BOUNDED cavities, not tori).

Here: a single +1 whorl on a bounded disc with a winding-1 boundary condition
(carries the net charge; no annihilation partner), a pinning well OFF-CENTER at
(2.5, 0). Question: under the Dirac weight W=(1+tau*beta)^2, does the lone whorl
stay pinned at the well, or drift to the symmetric centre?

Results (tau=0.5):
  - net interior charge Q = +1.00 in every run (a periodic torus forces 0)
  - the lone whorl SURVIVES under the Dirac weight (clean core, depth ~0.00)
  - the off-center well pins it off the symmetric centre (dist_to_well ~0.9,
    dist_to_centre ~1.6), looser than baseline (~0.68) but clearly held
  => the torus "clean kill" (0/4) was largely a pair-annihilation artifact.

Still open: the Dirac-OPERATOR index (overlap/Ginsparg-Wilson) on this
background, whose zero-mode count should equal +1 if the identification is real.

Do not hype. Do not lie. Just show.
PerceptionLab / Antti Luode, with Claude (Opus 4.8). June 2026.
"""
import numpy as np

N=128; Lx=16.0; dx=Lx/N; tau=0.5; mu=0.0004; TWO_PI=2*np.pi
xs=np.linspace(-Lx/2,Lx/2,N); Xg,Yg=np.meshgrid(xs,xs)
R_clamp=6.0; WELL=(2.5,0.0)
r_origin=np.hypot(Xg,Yg)
clamp = r_origin>R_clamp
clamp_val = np.exp(1j*np.arctan2(Yg,Xg))          # winding-1 boundary (carries net charge)
interior = r_origin < (R_clamp-0.3)

def lap(f): return (np.roll(f,1,0)+np.roll(f,-1,0)+np.roll(f,1,1)+np.roll(f,-1,1)-4*f)/dx**2
def biharm(f): return lap(lap(f))
def wrap(d): return (d+np.pi)%TWO_PI-np.pi
def vfield(phi):
    ph=np.angle(phi)
    d1=wrap(np.roll(ph,-1,1)-ph);d2=wrap(np.roll(np.roll(ph,-1,0),-1,1)-np.roll(ph,-1,1))
    d3=wrap(np.roll(ph,-1,0)-np.roll(np.roll(ph,-1,0),-1,1));d4=wrap(ph-np.roll(ph,-1,0))
    return (d1+d2+d3+d4)/TWO_PI
def net_interior_charge(phi): return float(vfield(phi)[interior].sum())
def core_pos(phi):
    a=np.abs(phi).copy(); a[~interior]=9.9
    i=np.unravel_index(np.argmin(a),a.shape); return Xg[i],Yg[i],a[i]

def m2_field(use_well,A=0.9,w=1.0):
    m2=np.ones((N,N))
    if use_well: m2-=A*np.exp(-((Xg-WELL[0])**2+(Yg-WELL[1])**2)/(2*w**2))
    return np.clip(m2,0.02,1.0)
def seed():
    ph=np.arctan2(Yg-WELL[1],Xg-WELL[0])
    amp=np.tanh(np.hypot(Xg-WELL[0],Yg-WELL[1])/0.7)
    phi=amp*np.exp(1j*ph); phi[clamp]=clamp_val[clamp]; return phi

def run(weight,use_well,T=110.0,nu=0.04,seed_noise=0.02,rng=None):
    rng=np.random.default_rng(0) if rng is None else rng
    m2=m2_field(use_well); phi=seed()
    phi[interior]+=seed_noise*(rng.standard_normal(phi.shape)+1j*rng.standard_normal(phi.shape))[interior]
    pif=np.zeros_like(phi)
    W0=(1+tau)**2 if weight=='dirac' else 1.0
    dt=0.30*dx/(np.sqrt(max(W0,2.25))*np.sqrt(2)); steps=int(T/dt)
    traj=[]
    for t in range(steps):
        b=np.abs(phi)**2
        W=1.0/(1.0+tau*b) if weight=='base' else (1.0+tau*b)**2
        acc=W*lap(phi)-(b-m2)*phi-nu*pif-mu*biharm(phi)
        pif+=dt*acc; phi+=dt*pif
        phi[clamp]=clamp_val[clamp]; pif[clamp]=0
        if not np.isfinite(np.max(np.abs(phi))): return dict(blew=True)
        if t%max(1,steps//40)==0:
            cx,cy,cd=core_pos(phi)
            traj.append((t/steps,cx,cy,cd,net_interior_charge(phi),
                         np.hypot(cx-WELL[0],cy-WELL[1]),np.hypot(cx,cy)))
    return dict(blew=False,traj=np.array(traj),phi=phi)

if __name__=="__main__":
    print("Lone whorl on bounded disc, well off-centre at (2.5,0). tau=0.5\n")
    for weight in ['base','dirac']:
        for uw in [True,False]:
            r=run(weight,uw)
            if r['blew']: print(f"  {weight} well={uw}: BLEW UP"); continue
            f=r['traj'][-1]
            print(f"  {weight:5s} well={str(uw):5s}: core=({f[1]:+.2f},{f[2]:+.2f}) "
                  f"dist_well={f[5]:.2f} dist_centre={f[6]:.2f} Q={f[4]:+.2f} depth={f[3]:.2f}")

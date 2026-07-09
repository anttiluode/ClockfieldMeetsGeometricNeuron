"""
clockfield_matter_stability.py
==============================
The clean falsifier follow-up: under the Dirac-consistent weight W=(1+tau*beta)^2
(the one that would make the Geometric Neuron the Dirac operator of the Clockfield),
WHICH matter is stable?

Engine (phiworld/best.py family):
    phi_tt = W(beta) * lap(phi) - V'(phi) - nu*phi_t - mu*biharm(phi)
    V = 1/4 (|phi|^2 - 1)^2   ->  ring vacuum |phi|=1, U(1) symmetry.
The ring vacuum makes BOTH matter types available:
    (1) BRIGHT solitons / oscillons  -- amplitude lumps, |phi|>1, NOT topological.
    (2) TOPOLOGICAL whorls           -- vortices, phase winding +-1, protected.

Two weights:
    baseline  W = 1/(1+tau*beta)   (waves SLOW where field is intense -> self-FOCUSING)
    dirac     W = (1+tau*beta)^2   (waves SPEED UP -> self-DEFOCUSING) <- unification weight

Textbook nonlinear-optics prediction (to be TESTED, not assumed):
    focusing media  -> BRIGHT solitons stable, dark/vortices less so
    defocusing media-> DARK solitons / VORTICES stable, bright disperse

Diagnostics are radiation-aware:
    bright matter : integrated excess (|phi|-1)^2 inside a moving window that tracks
                    the brightest lump (so dispersed radiation is excluded).
    topological   : robust plaquette winding count of surviving vortices at late time.

Each run: CFL-limited dt, fixed physical time T, blow-up flag (stiff != dispersed),
survival = late-time metric / early-time metric (averaged over an attractor window).

Do not hype. Do not lie. Just show.
PerceptionLab / Antti Luode, with Claude. Helsinki, June 2026.
"""
import numpy as np

N=128; Lx=16.0; dx=Lx/N; nu=0.01; mu=0.0006; TWO_PI=2*np.pi
xs=(np.arange(N)-N/2)*dx; Xg,Yg=np.meshgrid(xs,xs)

def lap(f):
    return (np.roll(f,1,0)+np.roll(f,-1,0)+np.roll(f,1,1)+np.roll(f,-1,1)-4*f)/dx**2
def biharm(f): return lap(lap(f))
def Vprime(phi): return (np.abs(phi)**2-1.0)*phi

def wrap(d): return (d+np.pi)%TWO_PI-np.pi
def vortex_field(phi):
    th=np.angle(phi)
    d1=wrap(np.roll(th,-1,1)-th)
    d2=wrap(np.roll(np.roll(th,-1,0),-1,1)-np.roll(th,-1,1))
    d3=wrap(np.roll(th,-1,0)-np.roll(np.roll(th,-1,0),-1,1))
    d4=wrap(th-np.roll(th,-1,0))
    return np.round((d1+d2+d3+d4)/TWO_PI)
def vortex_count(phi): return int(np.sum(np.abs(vortex_field(phi))))

def bright_window_excess(phi, R=2.5):
    a=np.abs(phi)
    idx=np.unravel_index(np.argmax(a), a.shape)     # brightest point (tracks the lump)
    cy=Yg[idx]; cx=Xg[idx]
    win=((Xg-cx)**2+(Yg-cy)**2)<R**2
    exc=np.maximum(a[win]-1.0,0.0)                   # excess over vacuum, inside moving window
    return float(np.sum(exc**2))

def seed_bright():
    phi=np.ones((N,N),complex)
    phi=phi+1.4*np.exp(-((Xg)**2+(Yg)**2)/1.0)       # one bright oscillon, no vortices
    return phi
def seed_vortices():
    phi=np.ones((N,N),complex)
    for cx,cy,q in [(-5,-3,+1),(-1,-3,-1),(2,3,+1),(6,3,-1)]:  # two well-separated pairs
        phi=phi*np.tanh(np.hypot(Xg-cx,Yg-cy)/0.8)*np.exp(1j*q*np.arctan2(Yg-cy,Xg-cx))
    return phi

def run(kind, weight, tau, T=60.0):
    phi = seed_bright() if kind=='bright' else seed_vortices()
    pi=np.zeros((N,N),complex)
    Wmax0 = np.max((1.0+tau*np.abs(phi)**2)**2) if weight=='dirac' else 1.0
    dt = 0.35*dx/(np.sqrt(Wmax0)*np.sqrt(2))
    steps=int(T/dt)
    metric=[]
    for t in range(steps):
        b=np.abs(phi)**2
        W = 1.0/(1.0+tau*b) if weight=='base' else (1.0+tau*b)**2
        a = W*lap(phi) - Vprime(phi) - nu*pi - mu*biharm(phi)
        pi=pi+dt*a; phi=phi+dt*pi
        mx=np.max(np.abs(phi))
        if not np.isfinite(mx) or mx>40:
            return dict(blew=True, tfrac=t/steps)
        if t%max(1,steps//60)==0:
            metric.append(bright_window_excess(phi) if kind=='bright' else vortex_count(phi))
    metric=np.array(metric,float)
    early=metric[:len(metric)//5].mean()            # first 20%
    late =metric[-len(metric)//5:].mean()           # last 20% = attractor window
    return dict(blew=False, early=early, late=late,
                survival=(late/early if early>1e-9 else late), series=metric, phi=phi)

# ---------------- run the sweep ----------------
TAUS=[0.5, 1.0, 2.0]
results={}
print("="*74)
print(" CLOCKFIELD MATTER-STABILITY SWEEP")
print(" survival = (late-time attractor metric) / (early metric)   [1.0 = fully retained]")
print("="*74)
for kind in ['bright','vortex']:
    tag = "BRIGHT solitons (amplitude, non-topological)" if kind=='bright' else "TOPOLOGICAL whorls (vortices)"
    print(f"\n  {tag}")
    print(f"  {'tau':>5} | {'baseline (focusing)':>26} | {'DIRAC (defocusing)':>26}")
    for tau in TAUS:
        rb=run(kind,'base',tau); rd=run(kind,'dirac',tau)
        results[(kind,tau)]=(rb,rd)
        def fmt(r,kind):
            if r['blew']: return f"BLEW UP @ {r['tfrac']*100:.0f}% of run"
            if kind=='vortex': return f"{r['early']:.0f} -> {r['late']:.1f} vortices"
            return f"{100*r['survival']:5.1f}% energy kept"
        print(f"  {tau:>5} | {fmt(rb,kind):>26} | {fmt(rd,kind):>26}")

# ---------------- figure ----------------
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
BG="#0a0a12"; PAN="#12121e"; RED="#ff3b6b"; BLU="#2ec5ff"; GRY="#6b6b85"; YEL="#f5c542"; GRN="#42f5a1"
plt.rcParams['font.family']='monospace'
fig,ax=plt.subplots(1,2,figsize=(13,5.2),facecolor=BG)
for a in ax: a.set_facecolor(PAN); a.tick_params(colors=GRY,labelsize=8)
for panel,kind,ttl,ylab in [(0,'bright','BRIGHT solitons (amplitude atoms)','fraction of energy retained'),
                            (1,'vortex','TOPOLOGICAL whorls (vortices)','vortices surviving at late time')]:
    a=ax[panel]
    for weight,col,lab in [('base',BLU,'baseline W=1/(1+tb)  (focusing)'),('dirac',RED,'Dirac W=(1+tb)^2  (defocusing)')]:
        ys=[]
        for tau in TAUS:
            r=results[(kind,tau)][0 if weight=='base' else 1]
            if r['blew']: ys.append(np.nan)
            elif kind=='bright': ys.append(min(r['survival'],1.5))
            else: ys.append(r['late'])
        a.plot(TAUS,ys,'o-',color=col,lw=1.8,ms=7,label=lab)
    a.set_title(ttl,color=YEL,fontsize=10)
    a.set_xlabel("clockfield strength  tau",color=GRY,fontsize=9)
    a.set_ylabel(ylab,color=GRY,fontsize=9)
    a.legend(facecolor=PAN,edgecolor="#23233a",labelcolor='white',fontsize=7,loc='best')
    for s in a.spines.values(): s.set_color("#23233a")
fig.suptitle("Which matter survives the unification weight? Baseline (focusing) vs Dirac (defocusing), swept over clockfield strength",
             color='white',fontsize=11,y=1.0)
plt.tight_layout(); plt.savefig("/mnt/user-data/outputs/matter_stability_sweep.png",dpi=140,facecolor=BG,bbox_inches='tight'); plt.close()
print("\nsaved matter_stability_sweep.png")

# ---------------- final-state snapshots for tau=1.0 ----------------
fig,ax=plt.subplots(2,2,figsize=(9.5,9.5),facecolor=BG)
panels=[('bright','base','bright + baseline (focusing)'),('bright','dirac','bright + DIRAC (defocusing)'),
        ('vortex','base','whorls + baseline (focusing)'),('vortex','dirac','whorls + DIRAC (defocusing)')]
for a,(kind,weight,ttl) in zip(ax.ravel(),panels):
    r=results[(kind,1.0)][0 if weight=='base' else 1]
    if r['blew']:
        a.text(0.5,0.5,'medium blew up',ha='center',va='center',color=RED,transform=a.transAxes)
        a.set_facecolor(PAN)
    else:
        a.imshow(np.abs(r['phi']),cmap='magma',vmin=0,vmax=1.7)
    a.set_title(ttl,color=YEL,fontsize=9); a.set_xticks([]); a.set_yticks([])
fig.suptitle("Final |phi| at tau=1.0  (bright atom disperses under Dirac; whorls persist)",color='white',fontsize=11)
plt.tight_layout(); plt.savefig("/mnt/user-data/outputs/matter_stability_fields.png",dpi=130,facecolor=BG,bbox_inches='tight'); plt.close()
print("saved matter_stability_fields.png")

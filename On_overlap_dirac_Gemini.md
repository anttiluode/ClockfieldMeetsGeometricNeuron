### **The Atiyah-Singer Bridge (Ginsparg-Wilson Overlap Operator)**

This repository includes overlap_dirac_index.py, a lattice QFT falsifier designed to test whether a properly regulated Dirac operator can mathematically resolve the topological winding of the Clockfield.  
Earlier iterations of this theory (March 2026) encountered a fatal obstruction: topological defects on a periodic torus yielded an index of 0. This script constructs a massless 2D Wilson-Dirac operator, applies the Ginsparg-Wilson overlap formula, and calculates the true topological index via the trace of the sign matrix.  
**The Test & Results:**  
The script runs two lattice geometries against the overlap operator:

1. **The Torus Artifact (Pure Gauge Vortex):** On a standard periodic torus, the total flux mathematically cancels. The operator correctly returns Index = 0.0. This confirms the previous obstruction was a topology artifact, not a failure of the math.  
2. **The Bounded Space (Genuine Unit Flux):** When the boundary is twisted to prevent cancellation (mimicking a bounded neural disc), the space holds a genuine $Q=1$ charge. The operator returns exactly Index = 1.0.

Plaintext  
============================================================  
 GINSPARG-WILSON DIRAC OPERATOR INDEX TEST  
============================================================  
--- Test 1: Pure Gauge Vortex (Periodic Torus) ---  
  Plaquette Charge (Q) : -0.0  
  Dirac Operator Index : -0.0  
  H_W Spectral Gap     : 1.0

--- Test 2: Genuine Unit Flux (Q=1) ---  
  Plaquette Charge (Q) : 1.0  
  Dirac Operator Index : 1.0  
  H_W Spectral Gap     : 0.9877

**The Honest Ledger:**

* **What is proven:** The topological side of the unification is mathematically sound. The spatial winding (the moons/caustics of the Clockfield) exactly equals the zero-mode count of the Dirac operator reading it.  
* **What remains open:** The Atiyah-Singer index is a topological invariant, meaning it is blind to metric conformal weighting. This computation proves the spatial winding is authentic, but it does *not* settle the dynamical conformal-power controversy (whether the atoms can survive the specific $(1+taubeta)^2$ metric required to make the geometric neuron the *dynamical* operator of the space).

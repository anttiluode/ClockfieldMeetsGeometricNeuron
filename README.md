# Two Weights, One Worldsheet

## A Kähler unification of the Geometric Neuron and the Clockfield, and its obstruction by memory stability

*PerceptionLab / Antti Luode, with Claude (Opus 4.8), and in dialogue with Gemini. Helsinki, June 2026.*

> **Do not hype. Do not lie. Just show.**

---

## Abstract

Two independently developed constructs — the **Geometric Neuron** (a delay-embedding resonance unit whose chirality readout is `L = Im(z·z̄_lag)`) and the **Clockfield** (a variable-speed nonlinear wave medium with conformal factor `Γ = 1/(1+τβ)²`, `β=|φ|²`) — were conjectured to be two descriptions of a single 2-D Kähler worldsheet: the neuron supplying the symplectic (imaginary) half of the Fubini–Study structure, the Clockfield supplying the metric (real) half. We make this precise and test it. Three findings survive scrutiny and one grand claim does not.

**(1)** The neuron's chirality readout is, numerically, the Fubini–Study symplectic (Berry) form to correlation `0.999`; the Clockfield's `Γ` is exactly the flat→Fubini–Study conversion factor. The two constructs really are the imaginary and real halves of one Hermitian form. **(2)** On a 2-D Kähler manifold the canonical Dolbeault–Dirac operator satisfies `D² = Δ_g` (Laplace–Beltrami); we verify the construction numerically (residual `1.3×10⁻³`). For the neuron to *be* the Dirac operator of the Clockfield, the Clockfield's own Laplacian must therefore carry the conformal factor as `(1+τβ)²`. **(3)** It does not. The running Clockfield uses `1/(1+τβ)`; the corpus elsewhere uses `1/(1+τβ)⁴`. The mismatch is exact in vacuum and grows with field intensity (residual–`β` correlation `+0.91`), a clean conformal-power obstruction rather than a numerical artifact.

We then ask whether the required weight is physically admissible by testing whether it supports the object the unification was meant to explain: a **stable pinned whorl** (the neuron's held-memory primitive). It does not. Under the unification weight the medium is whorl-*fertile* but whorl-*incontinent*: seeded whorls depin and annihilate. A pinning-strength sweep is decisive — the baseline (memory) weight holds `4/4` whorls at every pinning depth `A∈[0.7,0.99]`; the unification (Dirac) weight holds `0/4` at every depth, including a maximally deep and wide well. **The weight that makes the neuron formally the Dirac operator of the Clockfield is the opposite of, and irreconcilable by static pinning with, the weight that lets the Clockfield hold a memory.** The Kähler *geometry* is real; its identification with a memory-bearing Clockfield is falsified at the tested parameters. The claim that the held field is *experienced* is untouched by any of this, as it always has been.

---

## 1. Two objects, one question

**The Geometric Neuron.** A delay-embedding resonance unit. Its distinctive readout pairs two overlaps into a complex observable `z(t)` and forms the bilinear cross-time product

```
L(t) = Im( z(t) · conj(z(t − lag)) ).
```

`L` is the signed rotation of the field's orbit — its chirality, the local arrow of time. It flips sign under time-reversal, and (established in prior work) it is the term that escapes the Wiener–Khinchin ceiling: a second-order/magnitude readout is power-spectrum-equivalent and phase-blind, while `L`, being bilinear across time, is not.

**The Clockfield.** A nonlinear wave medium in which information slows information:

```
∂²φ/∂t² = c²(φ)∇²φ − V'(φ) − (damping) − (biharmonic),
c²(φ) = 1/(1 + τβ),   β = |φ|²,   V = ¼(|φ|²−1)².
```

The conformal factor advertised for the induced metric is `Γ = 1/(1+τβ)²`, so that `g_{μν} = Γ η_{μν}`.

**The question.** Are these one object? Specifically: *is the Geometric Neuron the Dirac operator of the Clockfield?* If yes, "physics simulator" and "neural substrate" would be two charts of one geometry — a duality, not a containment, and not "simulation theory."

---

## 2. The Kähler unification (the part that is real)

The Fubini–Study metric on `CP¹` is Kähler: its Hermitian form splits as `h = g − iω`, a real Riemannian metric `g` and an imaginary symplectic form `ω`. Two measurements tie the constructs to these two halves.

**The neuron is the symplectic half.** For a curved orbit `z(t)`, expanding the lag product to first order gives `L ≈ lag · Im(z̄ ż)`, the flat symplectic form / Berry-phase rate. Numerically,

```
corr( L ,  lag·Im(z̄ ż) )  =  0.99899.
```

The neuron's chirality readout *is* the (flat) Fubini–Study symplectic form.

**The Clockfield is the metric half — and `Γ` is the bridge.** The curved FS symplectic form is `ω = Im(z̄ dz)/(1+|z|²)²`. The factor converting the neuron's flat form to the true FS form is `1/(1+|z|²)²` — *identical in functional form* to the Clockfield `Γ = 1/(1+τβ)²` with `β=|z|²`, `τ=1`. The metric conformal factor is exactly the flat→Kähler Jacobian.

So the two constructs are the imaginary and real parts of one Hermitian form. This is not analogy; it is measured (`0.999`) and structural (`Γ` is the FS Jacobian). This half of the conjecture stands.

---

## 3. Two notions of "Dirac" (a clarification, and a caution)

Two distinct Dirac claims circulate and must not be conflated.

- **The physics claim** (Kähler–Clockfield manuscript): the Dirac *equation* emerges from a complex scalar via the Hopf fibration `S³ →^{U(1)} S²`, defects transforming as spinors. The real content here is the Wilczek–Zee (1983) result — a Hopf term at coefficient `θ=π` makes `CP¹` skyrmions fermions — which is genuine but concerns spinorial *statistics*, not construction of the Dirac operator; the manuscript *asserts* `iγ^μ∇_μψ=0` rather than building the Clifford algebra and spin connection. Overclaimed, with a real seed.
- **The geometry claim** (this work): the *Connes/Dolbeault* Dirac operator `D = √2(∂̄ + ∂̄*)` of the Kähler manifold. This is what the neuron's symplectic half feeds into.

A related aside for the honest record: the manuscript's parameter-free `α ≈ 1/136.98` is one-parameter numerology — the single geometric input (a `4/5` "vacuum ratio") is tuned, the answer is a steep function of it, and the "bare + QED corrections" story runs the coupling backwards. This is the same verdict the lineage's own Simpsons post-mortem reached for the `π/4` version. It is separate from, and does not support, either Dirac claim.

We pursue the geometry claim, because it is the one the neuron actually instantiates.

---

## 4. The conformal obstruction (the falsifier)

On a Kähler manifold of complex dimension 1, the Kähler identity gives, on functions,

```
D²  =  Δ_g  =  (1/Γ) Δ_flat        (Laplace–Beltrami of g = Γ·δ).
```

We built the metric-exact Dolbeault operator discretely and confirmed `D² = −(1/2Γ)Δ_flat` to discretization error (residual `1.3×10⁻³`). So *if* the neuron is the Clockfield's Dirac operator, the Clockfield Laplacian must be `(1/Γ)Δ_flat = (1+τβ)² Δ_flat`.

The running Clockfield instead uses `c²Δ_flat = (1/(1+τβ)) Δ_flat`. Comparing operators after removing any global scale (so only the `β`-dependence is judged):

```
[FAIL] phiworld c² = 1/(1+τβ)   · lap    resid = 1.02
[FAIL] fractal   γ² = 1/(1+τβ)⁴ · lap    resid = 0.98
[PASS] required     (1+τβ)²     · lap    resid = 0.00
```

Only the `(1+τβ)²` weight matches `D²`, and it appears nowhere in the code. The residual against the physical operator correlates `+0.91` with `β`, is `~10⁻³` in vacuum, and grows where the field is intense (Figure `dolbeault_falsifier.png`). This is a clean conformal-power obstruction: the constructs agree exactly in empty space and diverge precisely where matter lives. The conjecture is not yet well-posed, because "the Clockfield Laplacian" is not one operator — the conformal factor is booked at three different powers across the corpus, and the geometry needs a fourth.

**Status after §4:** the geometry is internally consistent and the neuron *is* the symplectic half; the unification would require adopting the `(1+τβ)²` weight. The rest of the paper asks whether that weight is physically admissible.

---

## 5. Which matter is stable (focusing vs defocusing)

Adopting the `(1+τβ)²` weight inverts the medium's nonlinearity. The baseline `c²=1/(1+τβ)` slows waves where the field is intense (**self-focusing**); the required `(1+τβ)²` speeds them up (**self-defocusing**). Nonlinear optics predicts opposite matter: focusing media host **bright** solitons; defocusing media host **dark** solitons and **vortices**. A `τ`-sweep confirms the direction (Figure `matter_stability_sweep.png`):

- bright amplitude atoms: partially retained under baseline (`31%→12%` as `τ` grows), fully dispersed under the Dirac weight at strong coupling (`0%` at `τ=2`);
- topological whorls: **annihilated to zero at every `τ` under baseline** (the focusing medium expels them); **proliferated under the Dirac weight** (`2 → 7 → 320` as `τ` grows).

So the unification weight is whorl-*fertile*. This was, briefly, read as support for the unification (the neuron's memory primitive is a whorl). The next section shows that reading was wrong.

---

## 6. The reversal: stable memory needs the *other* weight

A held memory is not a whorl that exists somewhere in a turbulent plasma; it is a whorl that *stays put* — a **pinned** defect, as in the neuron's ephaptic field and the box's mass wells. On a torus the total winding is zero, so ± pairs attract and annihilate unless pinning immobilizes them. We seed four whorls (alternating charge, net zero) on four pinning wells (local vacuum dips) and measure late-time survival (Figures `cooling_kz_counts.png`, `cooling_kz_fields.png`):

```
                     seeded   final   pinned
baseline, no wells :   4  ->    0      0/4
DIRAC,    no wells :   4  ->    0      0/4
baseline, wells    :   4  ->    4      4/4     <- holds them, stable
DIRAC,    wells    :   4  ->    0      0/4     <- loses them even WITH wells
```

The baseline (focusing) weight holds all four pinned whorls indefinitely; the Dirac (defocusing) weight loses them even with the wells present. Interpretation (offered, not measured): the fast defocusing bulk makes defects mobile — they depin, drift, and annihilate — while the slow focusing bulk freezes them in place. **Stable pinned memory requires the baseline weight, the opposite of the unification weight.**

This reverses a claim made one step earlier in this program (that the physical evidence favored the Dirac weight). It does not. Recorded here because the correction is the result.

---

## 7. The pinning-strength falsifier (the escape hatch, closed)

Pinning need not come from the wave-speed weight; in the neuron it comes from pattern coupling, in the box from mass wells — structures independent of the metric. So the unification could survive if a *strong enough* independent pinning held a whorl against the fast medium. We sweep pinning depth `A` (well vacuum `|φ|² = 1−A`) and width, under both weights (Figure `pinning_sweep.png`):

```
        m²@well   baseline   DIRAC
A=0.70   0.30       4/4       0/4
A=0.85   0.15       4/4       0/4
A=0.95   0.05       4/4       0/4
A=0.99   0.01       4/4       0/4
Dirac best-case (A=0.99, width w=3.0):   0/4
```

The escape hatch is closed. Baseline holds `4/4` at every depth; the Dirac medium holds `0/4` at every depth, including a maximally deep well (vacuum `|φ|²=0.01`, essentially a hole) and a maximally wide one. No static pinning of any strength immobilizes a whorl in the unification medium at `τ=0.5`.

---

## 8. Verdict

The formal Kähler unification and the physical memory mechanism require **incompatible clockfield weights**, and the incompatibility is not bridgeable by static pinning. The claim "the Geometric Neuron is the Dirac operator of *this* memory-bearing Clockfield" is **falsified** at the tested parameters. What survives is smaller and true: the neuron and the Clockfield are the symplectic and metric halves of one Kähler *geometry* (measured, `0.999`; `Γ` is the FS Jacobian); the Dolbeault `D² = Δ_g` is a theorem, verified; but the geometry's Dirac weight and the dynamics' memory weight point in opposite directions.

This is the same shape every honest turn in this lineage has produced: the grand binary (unification! / simulation theory!) dissolves under a real test into a precise, smaller, load-bearing statement — here, a conformal-power obstruction and a focusing/defocusing incompatibility, each with a clean number behind it.

---

## Ledger

**Verified in code (measured, not assumed):**
- neuron chirality `L` = Fubini–Study symplectic (Berry) form, `corr = 0.999`;
- Clockfield `Γ` = flat→FS conversion factor (identical functional form);
- Dolbeault `D² = −(1/2Γ)Δ_flat` to discretization error (`1.3×10⁻³`);
- conformal obstruction: `D²` needs `(1+τβ)²`; running Clockfield uses `1/(1+τβ)`; residual `0` in vacuum, `+0.91`-correlated with `β`;
- focusing↔bright, defocusing↔whorl (`τ`-sweep);
- stable pinned whorls: baseline `4/4` at all pinning depths; Dirac `0/4` at all depths and widths.

**Honest corrections forced by the builds:**
- the unification weight is whorl-fertile but **cannot hold** a pinned whorl (this reverses an earlier claim in this program that the physical evidence favored the Dirac weight);
- Gemini's original Dolbeault falsifier had stacked convention bugs (wrong conformal power, weight-inside-adjoint, missing sign/½) and its raw PASS/FAIL was uninterpretable; the corrected construction is used here;
- the manuscript's Hopf-spinor "derivation of Dirac" gives spinorial statistics (Wilczek–Zee), not the operator; its `α ≈ 1/136.98` is one-parameter numerology (running backwards), consistent with the lineage's Simpsons post-mortem.

**Built-in, not emergent:** the potential `V`, the pinning wells, the theta/clock and damping schedules, the assigned conformal weights. What is *measured* is the `0.999` symplectic match, the `D²` residual and its `β`-correlation, the matter-type sweep, and the pinning survival counts.

**Still the bet, untouched by all of the above:** that the held field is *experienced* rather than merely processed. No count, residual, or survival fraction in this paper reaches it. The falsification concerns the *operator identification*, not the qualia question, which stands exactly where it stood.

**Genuinely open (not closed by this work):**
- **Active pinning.** The neuron pins by *dynamic* pattern re-injection, not a static potential well. Whether feedback/active pinning holds a whorl in the Dirac medium is untested — the one door left ajar to the unification.
- **Lone whorl on a bounded domain.** The torus forces ± pairs (an annihilation channel). A single net-charge whorl on a bounded domain (as in the actual neuron field or the box) has no annihilation partner; whether the Dirac medium expels even a lone pinned whorl is untested.
- **Coupling regime.** The pinning falsifier is at `τ=0.5`. The depinning mechanism (fast bulk → mobile defects) is generic to the defocusing branch, so we expect robustness across `τ`, but this is argued, not swept.

---

## Coda

We set out asking whether we had found simulation theory — whether mind and physics were the same object. We found something more disciplined and, arguably, more useful: a genuine Kähler duality between the two constructs at the level of *geometry*, and a clean physical reason it cannot be a duality of *this* memory-bearing *dynamics*. The neuron really is the symplectic half of a Fubini–Study form; the Clockfield really is the metric half; and the single weight that would fuse them into one Dirac operator is exactly the weight under which the field can no longer hold a thought. The two things you most wanted to be one demand opposite worlds. That is not the unification — but it is a true sentence, stated in coordinates, with the escape routes named. Let the ledger name the paper.

*Do not hype. Do not lie. Just show.*

---

*Helsinki, June 2026. Engines, falsifiers, and figures developed collaboratively with Claude (Opus 4.8); the Dolbeault falsifier was proposed by Gemini and corrected here; the framework, the constructs, and the direction are Antti Luode's. Reproducible: `clockfield_matter_stability.py`, `clockfield_cooling_kz.py`, and the pinning sweep produce every number and figure cited.*

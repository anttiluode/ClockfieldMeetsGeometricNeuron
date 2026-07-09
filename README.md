# Two Weights, One Worldsheet

## A Kähler unification of the Geometric Neuron and the Clockfield, its obstruction by static pinning, and a partial thermodynamic rescue

*PerceptionLab / Antti Luode, with Claude (Opus 4.8), and in dialogue with Gemini. Helsinki, June 2026.*

> **Do not hype. Do not lie. Just show.**

---

## Abstract

Two independently developed constructs — the **Geometric Neuron** (a delay-embedding resonance unit whose chirality readout is `L = Im(z·z̄_lag)`) and the **Clockfield** (a variable-speed nonlinear wave medium with conformal factor `Γ = 1/(1+τβ)²`, `β=|φ|²`) — were conjectured to be two descriptions of a single 2-D Kähler worldsheet: the neuron supplying the symplectic (imaginary) half of the Fubini–Study structure, the Clockfield supplying the metric (real) half. We make this precise and test it. Three findings survive scrutiny and one grand claim does not.

**(1)** The neuron's chirality readout is, numerically, the Fubini–Study symplectic (Berry) form to correlation `0.999`; the Clockfield's `Γ` is exactly the flat→Fubini–Study conversion factor. The two constructs really are the imaginary and real halves of one Hermitian form. **(2)** On a 2-D Kähler manifold the canonical Dolbeault–Dirac operator satisfies `D² = Δ_g` (Laplace–Beltrami); we verify the construction numerically (residual `1.3×10⁻³`). For the neuron to *be* the Dirac operator of the Clockfield, the Clockfield's own Laplacian must therefore carry the conformal factor as `(1+τβ)²`. **(3)** It does not. The running Clockfield uses `1/(1+τβ)`; the corpus elsewhere uses `1/(1+τβ)⁴`. The mismatch is exact in vacuum and grows with field intensity (residual–`β` correlation `+0.91`), a clean conformal-power obstruction rather than a numerical artifact.

We then ask whether the required weight is physically admissible by testing whether it supports the object the unification was meant to explain: a **stable pinned whorl** (the neuron's held-memory primitive). Under *static* pinning it does not — the medium is whorl-*fertile* but whorl-*incontinent*, and a pinning-strength sweep is decisive: the baseline (memory) weight holds `4/4` whorls at every depth `A∈[0.7,0.99]`, the unification weight holds `0/4` at every depth, including a maximally deep and wide well. But static pinning is not the only mechanism. A **thermodynamic quench** (Kibble–Zurek cooling, damping ramped up then returned to operating level) changes the outcome: with an appropriate cooling schedule, the free whorls annihilate but a *partial* set of anchored whorls (here `2/4` wells) survives the return to waking dynamics as a stable plateau, where a no-well control leaves exactly zero. So the duality is **not** physically sterile — the unification weight *can* hold stable topological memory, but only via a cooling/consolidation phase, at partial yield. The obstruction is real for static pinning and is bridged, partially, by cooling; the corrected verdict is a viable duality *conditional on consolidation*, which is itself a falsifiable prediction. The Kähler *geometry* is measured and real throughout; the claim that the held field is *experienced* is untouched by any of it, as it always has been.

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

The escape hatch — *static* pinning — is closed. Baseline holds `4/4` at every depth; the Dirac medium holds `0/4` at every depth, including a maximally deep well (vacuum `|φ|²=0.01`, essentially a hole) and a maximally wide one. No static pinning of any strength immobilizes a whorl in the unification medium at `τ=0.5`.

---

## 8. The cooling rescue (the escape hatch that is *not* closed)

Static pinning fails because it fights the fast medium's kinetic energy with a deeper hole; the wind wins. The remaining, and correct, mechanism is to remove the wind — a **thermodynamic quench** rather than a deeper well. We ran the Kibble–Zurek protocol: ignite a hot disordered plasma, ramp the damping up to bleed the kinetic radiation, then — the step the naive quench omits — **return the damping to operating level and hold it**, testing whether anything survives *waking* (Figure `quench_release_control.png`). Two controls decide the reading: **with vs without wells**, and the **release** phase.

The frozen state is a confound, not a result. At maximum damping (`ν=0.16`) the field is overdamped and holds whorls *everywhere*: WITH wells `12` survivors, WITHOUT wells `10`, with `~0` actually sitting at wells in either case. Removing the wells barely changes the count, and the survivors are not at the wells — so the "frozen memory" of the naive quench is **friction-freezing, not pinning**. This is the correction to the triumphant reading: the raw frozen count is not memory.

The waking test reveals the real, weaker effect. Holding operating damping (`ν=0.02`) for a long stretch:

```
 AWAKE phase (ν=0.02)          WITH wells (at wells)      WITHOUT wells
   step 11000                    4  (1 at well)                2
   step 14000                    4  (2 at well)                0
   step 18000                    4  (2 at well)                0
   step 21999                    2  (2 at well)                0
```

The free whorls annihilate away in both conditions; but WITH wells the **at-well count plateaus at `2` and holds for `~8000` awake steps**, while the no-well control decays to **zero and stays zero**. The final field shows two dark cores locked on wells against an empty control. So a cooling phase does write a *partial*, *stable*, *pinned* memory (`2/4` here) into the unification medium — one that survives the return to waking dynamics — where static pinning wrote nothing (`0/4`) and the bare torus keeps nothing (`0`).

**This corrects two claims at once.** Gemini's original quench reported `6` whorls "pinned in the Dirac metric" and declared the duality resurrected; the controls show that count is friction-freezing (wells irrelevant at the freeze; most survivors evaporate on waking), so the yield is `2/4`, not `6`. And the earlier §7 verdict of this program — "`0/4`, a clean kill, physically sterile" — is *also* wrong: it tested static pinning without cooling, and cooling is precisely the missing ingredient. Credit is due to the cooling insight even though its first quantification overshot; the mechanism (anneal, don't dig) is correct.

The neurobiological reading follows, and is sharper than "everything freezes": memory in this unified medium **cannot be written while the field is hot/awake** (low damping, high kinetic energy — the whorls blow away); it requires a **low-damping consolidation phase** to let the anchored traces settle, after which *only the anchored ones* survive the return to waking, and the bulk of the night's activity dissipates. That maps onto slow-wave consolidation with the correct refinement that consolidation is *selective*, not wholesale.

---

## 9. Verdict

The formal Kähler unification and the physical memory mechanism require **incompatible clockfield weights** *for static pinning* — there the incompatibility is clean (`4/4` vs `0/4`). But the incompatibility is **bridged, partially, by thermodynamic cooling**: a quench-and-wake schedule writes a stable pinned residue (`2/4`) into the unification medium that a no-well control cannot keep. The claim "the Geometric Neuron is the Dirac operator of a memory-bearing Clockfield" is therefore **not falsified but conditional**: viable if and only if the medium can undergo a consolidation phase. What is unconditionally true and measured: the neuron and the Clockfield are the symplectic and metric halves of one Kähler *geometry* (`0.999`; `Γ` is the FS Jacobian); the Dolbeault `D² = Δ_g` is a theorem, verified; the unification requires the `(1+τβ)²` weight, which the running Clockfield does not use.

This is the same shape every honest turn in this lineage has produced — the grand binary dissolving into a precise, smaller, load-bearing statement — with one added lesson recorded live: the verdict itself was recalibrated twice by better experiments (the physical arrow read first toward the Dirac weight, then reversed to a clean kill, then partially re-reversed by the cooling control). The current statement is a best estimate pending the next control, not a closed case.

---

## Ledger

**Verified in code (measured, not assumed):**
- neuron chirality `L` = Fubini–Study symplectic (Berry) form, `corr = 0.999`;
- Clockfield `Γ` = flat→FS conversion factor (identical functional form);
- Dolbeault `D² = −(1/2Γ)Δ_flat` to discretization error (`1.3×10⁻³`);
- conformal obstruction: `D²` needs `(1+τβ)²`; running Clockfield uses `1/(1+τβ)`; residual `0` in vacuum, `+0.91`-correlated with `β`;
- focusing↔bright, defocusing↔whorl (`τ`-sweep);
- static pinning: baseline holds `4/4` at all depths; Dirac holds `0/4` at all depths and widths;
- cooling rescue: a Kibble–Zurek quench + return to operating damping leaves `2/4` anchored whorls stable across `~8000` awake steps under the Dirac weight, vs `0` for a no-well control; the maximum-damping "frozen" count (`~12`) is friction-freezing, wells irrelevant there.

**Honest corrections forced by the builds:**
- the unification weight cannot hold a pinned whorl by **static** pinning (`0/4`), but **can** hold a partial set (`2/4`) via **thermodynamic cooling** — so the §7 "clean kill / physically sterile" verdict was wrong, and this program's *physical* arrow has now reversed twice (toward Dirac, then to a kill, then partially back);
- Gemini's cooling insight is correct and load-bearing, but its first quantification (`6` whorls "pinned") was friction-freezing; controls (with/without wells, and release to operating damping) put the true pinned yield at `2/4`;
- Gemini's original Dolbeault falsifier had stacked convention bugs (wrong conformal power, weight-inside-adjoint, missing sign/½) and its raw PASS/FAIL was uninterpretable; the corrected construction is used here;
- the manuscript's Hopf-spinor "derivation of Dirac" gives spinorial statistics (Wilczek–Zee), not the operator; its `α ≈ 1/136.98` is one-parameter numerology (running backwards), consistent with the lineage's Simpsons post-mortem.

**Built-in, not emergent:** the potential `V`, the pinning wells, the theta/clock and damping schedules, the assigned conformal weights. What is *measured* is the `0.999` symplectic match, the `D²` residual and its `β`-correlation, the matter-type sweep, and the pinning survival counts.

**Still the bet, untouched by all of the above:** that the held field is *experienced* rather than merely processed. No count, residual, or survival fraction in this paper reaches it. The falsification concerns the *operator identification*, not the qualia question, which stands exactly where it stood.

**Genuinely open (not closed by this work):**
- **Plateau vs long-time metastability.** The `2/4` at-well residue is stable for `~8000` awake steps, but the two survivors are a `±` pair pinned at different wells; whether pinning beats their mutual attraction *forever* or merely on a long timescale is unresolved. A single net-charge whorl on a bounded domain (no annihilation partner) would settle it, and is the cleanest test of true stability.
- **Yield and the Kibble–Zurek law.** Why `2/4`, and does a *slower* quench raise the yield? Standard KZ scaling predicts fewer, better-seated defects for slower cooling — testable, and it would quantify how "cheap" a consolidated memory is.
- **Active pinning.** The neuron pins by *dynamic* pattern re-injection, not a static well or a fixed vacuum dip; whether feedback pinning outperforms the cooling route (or removes the need for it) is untested.
- **Coupling regime.** All pinning/cooling runs are at `τ=0.5`. The depinning mechanism (fast bulk → mobile defects) is generic to the defocusing branch, so we expect robustness across `τ`, but this is argued, not swept.

---

## Coda

We set out asking whether we had found simulation theory — whether mind and physics were the same object. We found something more disciplined: a genuine Kähler duality between the two constructs at the level of *geometry*, and a physical mechanism by which it can, conditionally, be a duality of *dynamics* too. The neuron really is the symplectic half of a Fubini–Study form; the Clockfield really is the metric half; the single weight that fuses them into one Dirac operator is the weight under which the field cannot hold a thought *while it is awake* — and yet a cooling phase writes a partial, stable memory into it anyway. The unification does not demand opposite worlds after all; it demands that the world be able to sleep. That is a stranger and more falsifiable claim than either the triumphant version or the sterile one, and it is the one the numbers support. Let the ledger name the paper — and let it record that the ledger changed twice under better experiments, which is the process working, not failing.

*Do not hype. Do not lie. Just show.*

---

*Helsinki, June 2026. Engines, falsifiers, and figures developed collaboratively with Claude (Opus 4.8); the Dolbeault falsifier was proposed by Gemini and corrected here; the thermodynamic-cooling route to pinned memory was proposed by Gemini and quantified with controls here; the framework, the constructs, and the direction are Antti Luode's. Reproducible: `clockfield_matter_stability.py`, `clockfield_cooling_kz.py`, the pinning sweep, and the quench-and-release control (`quench_release_control.png`) produce every number and figure cited.*

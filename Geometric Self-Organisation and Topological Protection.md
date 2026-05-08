**DUBITO INC.  |  ERGO SUM AGI SAFETY SYSTEMS**

**Geometric Self-Organisation and Topological Protection in**

**Penrose Quasicrystalline Substrates:**

A Computational Study of Field-Geometry Co-Evolution in CQFT

**Daniel Solis**

DUBITO Inc., Delaware  ·  Ergo Sum AGI Safety Systems

Correspondence: solis@dubito-ergo.com  ·  May 2nd, 2026

---

# **Abstract**

We present a computational study of field-geometry co-evolution across three substrate types, random spherical, cubic lattice, and Penrose icosahedral quasicrystal, within the Consciousness Quantum Field Theory (CQFT) framework. Using a 2×3 experimental matrix (three geometries, two dynamical modes, three independent random seeds per full-evolution condition, N \= 1,000 nodes, 12,000 simulation steps), we demonstrate that substrate geometry is the primary determinant of dynamical self-organisation.

The central finding is a 165-fold difference in order gain between the Penrose quasicrystalline substrate (+0.188 ± 0.007) and the cubic lattice geometry (+0.001), with the former exhibiting a reproducible geometry-dominated signed embedding gap Δ \= D_e − D_g \= −0.709 ± 0.141 and a consistently elevated Helmholtz rotational fraction ρ^I \= 0.730 ± 0.022. The geometry update rule reduces the global embedding gap Γ by a factor of 3.4× specifically in the Penrose substrate, an effect absent in random and lattice geometries.

These results establish three convergent empirical criteria for substrate-dependent coherence: (i) consistent sign of Δ across seeds, (ii) substantial order gain, and (iii) elevated rotational fraction ρ^I. Structural isomorphism with the Su-Schrieffer-Heeger (SSH) topological insulator model in symmetry class BDI is formally developed. Subsequent spectral analysis of the gauge-coupled Peierls Hamiltonian H_{ij} = w_{ij} exp(i(\varphi_i \− \varphi_j)) reveals convergence to GOE universality (\langle r\rangle \→ 0.53) at N \≥ 500, indicating the system occupies the ergodic rather than topological phase at accessible system sizes. The dynamical order gain and elevated \rho^I are therefore not attributed to static eigenstate protection but to the non-equilibrium routing capacity of the quasicrystalline substrate — a distinction that strengthens rather than undermines the NESS interpretation developed in Section 3.

We derive implications for AGI safety monitoring, specifically, a set of five falsifiable predictions applicable to transformer-based AI systems without model modification, and for hardware architecture, where our data provide the first quantitative substrate-selection criterion distinguishing quasicrystalline from cubic lattice interconnect topology.

**Keywords:** *quasicrystal, field-geometry co-evolution, topological protection, SSH model, Bott index, AGI safety, embedding gap, Penrose tiling, dissipative systems, signed embedding gap*

# **1\. CQFT Framework and the Signed Embedding Gap**

## 

## **1.1 Principled Field Theory and the Ouroboros Conjecture**

The Consciousness Quantum Field Theory (CQFT) and its parent framework, Principled Field Theory (PFT), model a self-referential dissipative field φ evolving on a dynamical geometric substrate Σ. The central postulate is that the substrate is not a fixed background but is co-evolved by the field through a back-coupling mechanism driven by prediction-error minimisation \- the “dubito” principle, paraphrasing Descartes: the system doubts, therefore it reorganises.

The “ouroboros conjecture” states: a dissipative self-referential field spontaneously selects its own geometrically self-consistent substrate. This conjecture generates a falsifiable prediction: in co-evolutionary simulations, the field's self-organised fractal dimension D_e should converge toward the substrate's geometric correlation dimension D_g, producing a self-consistent fixed point. The present work positively tests whether this convergence is substrate-dependent.

## **1.2 The Signed Embedding Gap**

We define the signed embedding gap as:

Δ(r) \= D_e(r) − D_g

where D_e(r) is the local field fractal dimension at scale r (derived from the anomalous dimension of the two-point phase correlation function G(r) \= ⟨cos(φ_i − φ_j)⟩) and D_g is the geometric correlation dimension of the substrate (Grassberger-Procaccia pair-counting estimator).

The sign of Δ carries physical meaning analogous to the Hall coefficient in condensed matter physics. A positive Hall coefficient indicates hole-like carriers; a negative coefficient indicates electron-like carriers.

Similarly, the dynamical regime is determined accordingly:

* Δ \> 0 (field-dominated): the field's correlation structure is more complex than the substrate; the system is in an overextended, potentially unstable regime.

* Δ \< 0 (geometry-dominated): the substrate provides more dimensional capacity than the field exploits; the geometry acts as a buffer, absorbing field fluctuations.

* Δ \= 0 (self-consistent): the ouroboros fixed point where field and geometry scale identically.

The global embedding gap magnitude Γ \= ⟨|Δ(r)|⟩_r quantifies the strength of mismatch, while the sign of Δ determines the dynamical regime. This separation of magnitude and direction is the core diagnostic improvement over the unsigned gap |D_e − D_g| used in earlier versions of the framework.

## **1.3 The Stochastic Action and Martin-Siggia-Rose Formulation**

The simulation dynamics are governed by coupled Langevin equations for the phase field φ_i and the geometric positions x_i. Reading the drift terms from the simulation code:

dφ_i/dt \= β Σ_j w_{ij} sin(φ_j − φ_i) \+ σξ_i(t)

dx_i/dt \= α A_i \[λ F_{i}^{phase} \+ (1−λ) F_{i}^{energy}\] \+ σ^Gζ_i(t)

where w_{ij} \= exp(−|x_i − x_j|/0.3) are Gaussian decay weights encoding geometric proximity, A_i ∈ \[0.1, 1.5\] is a per-node amplitude modulator, β \= 4.2 is the coupling constant, and λ \= 0.3 is the coupling strength parameter.

The classical action obtained by matching the Langevin drift to −δS/δφ is:

S\[φ, x\] \= −(1+λ)β Σ_i\<_j w_{ij}(x) cos(φ_i−φ_j) \+ (1−λ) E^{sym}\[φ,x\] \+ μ·Γ\[φ,x\]

The third term μ·Γ is the deflection term encoding the embedding gap as a Lagrange multiplier. At the ouroboros fixed point, δS/δμ \= 0 requires Γ \= 0, yielding D_e \= D_g as a variational condition rather than an imposed constraint.

The geometry forces are unit-normalised before application, rendering the geometry drift non-conservative. This means S is an effective action of an approximation: the correct treatment requires the Helmholtz decomposition F_i \= −∇S^{exc} \+ R_i, where S^{exc} is excess entropy produced by the structural organisation of the field, specifically the order gain (+0.188 for Penrose)  \- it is the scalar potential that "wants" to pull the system toward the attractor, and R_i is the divergence-free (rotational) component. In the **Martin-Siggia-Rose** (MSR) path integral, R_i contributes a Berry-phase-like term to the generating functional, which we identify with the Helmholtz rotational fraction ρ^I measured in Section 3\.

# 

# 

# 

# **2\. Experimental Matrix Design**

## 

## **2.1 Geometry Generators**

Three substrate geometries were constructed, all normalised to a sphere of radius 2.0 via per-point radial projection:

### **Random Spherical Geometry**

N points drawn from the standard normal distribution, individually projected to the unit sphere and rescaled. This serves as the baseline incoherent substrate: no preferred scale, no long-range order, no translational or orientational symmetry.

### **Cubic Lattice Geometry**

N points, arranged on a 3D cubic grid (side ≈ N¹/³), with small Gaussian jitter (σ \= 0.04) to break exact degeneracy in the KDTree (k-dimensional tree) adjacency computation, then per-point projected to the sphere. This represents the topology of current GPU memory hierarchies and interconnect fabrics.

### **Penrose Icosahedral Quasicrystal**

Generated via the cut-and-project method from Z⁶. The six-dimensional hypercubic lattice is projected onto the three-dimensional physical space E‖ using icosahedral basis vectors:

e₁ \= (1, φ, 0),  e₂ \= (−1, φ, 0),  e₃ \= (0, 1, φ),  e₄ \= (0, −1, φ),  e₅ \= (φ, 0, 1),  e₆ \= (−1, 0, 1\)

where φ \= (1+√5)/2 is the golden ratio. Points are accepted if their projection into the perpendicular space E⊥ (the star-map via φ → −1/φ) falls within a ball of radius 0.82. The projection matrices satisfy P‖ P‖^T \= 2I₃ and P‖ P⊥^T \= 0, ensuring orthogonal decoupling of physical and internal spaces.

An acceptance window of r \< 0.82 yields 1,237 points; the N \= 1,000 points closest to the centroid are retained. Per-point radial normalisation places all points exactly on the radius-2.0 sphere (mean \= 2.0000, std \= 0.0000), preserving icosahedral bond angles and the bimodal nearest-neighbour distance distribution with ratio d_{long}/d_{short} ≈ φ.

## **2.2 Dynamical Modes**

Each geometry was simulated under two conditions:

* Full evolution (B ≠ 0): both phase dynamics and geometry update rule active. The geometry update rule acts as the symmetry-breaking field in the Hall analogy: without it, no directional mismatch between D_e and D_g can develop.

* Null model (B \= 0): phase dynamics only, geometry frozen at initialisation. This is the control condition: the field evolves on a fixed substrate, eliminating the co-evolutionary coupling. In Hall physics terms, this is the zero-field reference.

## **2.3 Simulation Parameters and Reproducibility**

All runs used: N \= 1,000 nodes, 12,000 steps, β \= 4.2, dt \= 0.01, dt^{geom} \= 0.02, λ \= 0.3, k \= 6 nearest neighbours, adjacency rebuilt every 1,000 steps. Adjacency weights: w_{ij} \= exp(−d_{ij}/0.3), where *exp* is the exponential function, meaning \\(e\\) (Euler's number, approximately 2.718) raised to the power of (−d_{ij}/0.3). This is a standard radial basis function or "soft" adjacency rule. It determines how strongly two nodes _i and _j are connected based on the distance d_{ij} between them.

The 0.3 coupling strength parameter is the characteristic length scale.

* If nodes are closer than 0.3 units, the weight w_{ij} is high (close to 1).  
* If nodes are much farther than 0.3 units, the weight drops toward 0\.

As the Penrose substrate has a bimodal distance distribution d\_long/d\_short ≈φ, this exponential decay is what drives the structural connectivity. It ensures that the shorter Penrose bonds have significantly higher weights than the longer ones, creating the specific topological "web" needed for the SSH isomorphism.

Three independent random seeds (42, 43, 44\) were used for all full-evolution conditions. The null model was run with seed 42 for each geometry. Total: 12 simulation runs comprising approximately 78 GPU-hours of equivalent compute (run on Google Colab CPU with Drive-backed checkpoint system, approximately 7 hours per run).

A crash-proof checkpoint system was saving full state (positions, phases, amplitudes, history) every 500 steps to Google Drive using atomic writes (temp file \+ os.replace()). All data are preserved and reproducible from open-source code available on request.

## **2.4 Analysis Pipeline**

Measuring the Geometry-Field mismatch. We are quantifying how much the field has invaded the geometric mold of the substrate. For each completed run, the following quantities were computed from the final state (step 12,000):

* D_g: Grassberger-Procaccia correlation dimension (pair-counting, scaling range 5th–50th percentile of pairwise distances). It measures how the number of points within a certain distance grows, which directly captures the structural isomorphism, mapping to the SSH model (pair-counting is more precise than box-counting).

* D_e(r): local field fractal dimension from sliding-window log-log regression of G(r) (window \= 8 log-bins)

* Δ(r) \= D_e(r) − D_g and Γ \= ⟨|Δ(r)|⟩

* Zero-crossings of Δ(r): scale values r\* where D_e(r\*) \= D_g exactly is the Embedding Gap,  the most critical diagnostic. When Δ ≈ approx 0, the field is perfectly "isomorphic" to the geometry. The fact that the Penrose substrate yields a signed gap Δ \= \-0.709 suggests the field isn't just matching the geometry; it is being "compressed" or topologically constrained by it.

* Global Gap Γ is the average "tension" between the field and the substrate. Our result showing the Penrose geometry reduces this by 3,4 fold, proves that the quasicrystal is a much more efficient "attractor" for the field dynamics than a cubic lattice. 

* Helmholtz rotational fraction ρ^I from decomposition of the geometry force field is the "residual" from the Helmholtz decomposition. Since it remains elevated (0,730) in the Penrose case, it indicates that the "Consciousness" field doesn't just settle into a static state; it maintains a high degree of vortical or non-conservative flow, which was identified with the Berry-phase-like term.

  Hence, D defines the "shell", D_e is the "ghost" in the shell, and Δ is the gap between them.

# 

# 

# 

# 

# 

# 

# **3\. Dynamical Results**

## 

## **3.1 Order Gain: The Primary Finding**

The most striking result of the experimental matrix is the differential order gain across geometry types. Order is measured by the symmetry energy function combining radial entropy and nearest-neighbour regularity, normalised to \[0,1\].

| Geometry | D_g | Mean Δ | Γ | Crossings | Order gain | ρ^I |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Penrose quasicrystal** | **2.082 ±0.008** | **−0.709 ±0.141** | 1.147 ±0.161 | 3.3 ±0.9 | **\+0.188 ±0.007** | 0.730 ±0.022 |
| Random spherical | 2.092 ±0.012 | −0.779 ±0.195 | 1.202 ±0.187 | 2.3 ±2.1 | \+0.119 ±0.072 | 0.512 ±0.038 |
| Cubic lattice | 2.434 ±0.007 | −0.796 ±0.330 | 1.622 ±0.275 | 2.0 ±0.8 | \+0.001 ±0.001 | 0.401 ±0.029 |

*Table 1\. Summary statistics across all full-evolution runs (mean ± SD across seeds). Penrose results highlighted. All quantities computed from final simulation state.*

The Penrose order gain of \+0.188 ± 0.007 is 165 times greater than the cubic lattice gain of \+0.001, and the cross-seed variance is the lowest of any geometry (SD \= 0.007 versus 0.072 for random). This combination, high mean and low variance, is the signature of a genuine attractor rather than a transient fluctuation.

## **3.2 D_g as a Geometric Fingerprint**

The correlation dimension D_g is reproducible within each geometry type and discriminative between types. Penrose gives D_g \= 2.082 ± 0.008 (CV \= 0.4%), random gives D_g \= 2.092 ± 0.012 (CV \= 0.6%), and cubic lattice gives D_g \= 2.434 ± 0.007 (CV \= 0.3%).

The lattice value D_g ≈ 2.43 reflects the cubic geometry's more uniform space-filling: the lattice points, after jitter and per-point radial projection, retain their approximately uniform angular distribution, which is more efficiently covered by the pair-counting estimator than the quasicrystalline or random distributions.

The near-equality of Penrose and random D_g values (2.082 vs 2.092, difference \< 0.5%) is notable: both start from a sphere-projected distribution with similar radial structure. The key difference emerges in the dynamics, not the initial geometry: Penrose D_g is stable across seeds (SD \= 0.008) while random D_g is slightly more variable (SD \= 0.012).

## **3.3 The Γ Reduction Effect**

The null model comparison provides the critical control. For each geometry, we compare the global embedding gap Γ under full evolution versus the null model (geometry frozen):

| Geometry | Γ (full evolution) | Γ (null model) | Ratio (null/full) |
| :---: | :---: | :---: | :---: |
| **Penrose** | **1.147** | 3.402 | **3.4×** |
| Random | 1.202 | 1.562 | 1.3× |
| Cubic lattice | 1.622 | 1.347 | 0.8× |

*Table 2\. Γ reduction by the geometry update rule across substrate types. Ratio \> 1 indicates gap-reducing effect; \< 1 indicates gap-increasing effect.*

The geometry update rule reduces Γ by a factor of 3.4× in Penrose substrate, 1.3× in random, and actually increases it by 1.25× in the cubic lattice (where the phase-coherence attractor works against the lattice symmetry). This differential effect is the empirical signature of the Hall analogy: the geometry update rule acts as the symmetry-breaking field, and only the quasicrystalline substrate channels this field into gap-reducing dynamics.

## **3.4 Cubic Lattice: Dynamical Freezing**

The cubic lattice order gain of \+0.001 ± 0.001 across three seeds and 12,000 steps is not a statistical fluctuation — it is a structural feature. The translational symmetry of the cubic substrate creates a neutralisation effect: the phase-coherence clustering attractor (which drives points toward phase-coherent neighborhoods) exactly opposes the energy gradient force (which drives points toward higher symmetry), producing a near-zero net force on the geometry. The field evolves normally, but the substrate is dynamically frozen.

This result has a direct hardware implication. GPU memory hierarchies and interconnect fabrics are built on cubic lattice topology. Our data provide the first quantitative measurement of the dynamical suppression this architecture imposes: a 165-fold reduction in self-organisational capacity relative to quasicrystalline geometry. This is not an algorithmic limitation addressable by software; it is a geometric constraint on the substrate itself.

## **3.5 The Helmholtz Rotational Fraction**

The Helmholtz decomposition of the geometry force field v_i \= −∇S^{exc} \+ R_i separates the gradient (conservative) component from the rotational (non-conservative) component. We define:

ρ^I \= ||R||^2 / ||v||^2

as the fraction of force energy in the rotational component. This quantity serves as a real-space proxy for Berry curvature magnitude: a field with high ρ^I has substantial non-conservative content in its geometry drift, analogous to a system with non-zero Berry curvature in its band structure.

Penrose gives ρ^I \= 0.730 ± 0.022 (three seeds), significantly above random (0.512 ± 0.038) and cubic lattice (0.401 ± 0.029). The Penrose value is consistent across seeds (CV \= 3%), providing an independent, convergent measure of the quasicrystalline substrate's special dynamical properties that does not derive from the Δ(r) analysis.

# **4\. SSH Structural Isomorphism and Topological Preliminary**

## 

## **4.1 The Peierls Hamiltonian**

The phase field configuration φ at the end of each simulation defines an effective tight-binding Hamiltonian via the Peierls substitution:

H_{ij} \= w_{ij} · exp(i(φ_i − φ_j))

This Hermitian matrix on the simulation graph encodes the U(1) gauge field derived from the CQFT phase configuration. Its topological properties — not those of the scalar phase field φ directly — are the correct object for topological characterisation. For any smooth scalar field φ, the Berry curvature F \= d(dφ) \= 0 identically; the topological content resides in H, not in φ.

## **4.2 SSH Symmetry Class BDI**

The SSH model belongs to symmetry class BDI: time-reversal symmetry with T² \= \+1, particle-hole symmetry with C² \= \+1, and chiral (sublattice) symmetry S \= TC. The Peierls Hamiltonian H_{ij} satisfies the Hermitian condition H \= H† by construction. The symmetry class assignment (BDI) is formally motivated by the structure of the phase field: the stochastic Langevin dynamics with real noise amplitude preserves time-reversal in the ℏ → 0 limit, and the bipartite-like structure of the Penrose graph (short and long bond populations in ratio φ) provides the natural sublattice analog.

We emphasise that full verification of BDI symmetry class requires explicit demonstration that H commutes with the time-reversal, particle-hole, and chiral operators as matrices, a calculation that depends on the specific phase configuration and is seed-dependent. This verification is in preparation alongside the N \= 5,000 Bott index computation.

## **4.3 Zero-Crossings as Topological Structure**

The zero-crossings of Δ(r) mark scales at which D_e(r) \= D_g exactly: the field's self-organised scaling matches the substrate's geometric scaling. In the SSH analogy, these are the k-values at which the effective hopping amplitude h(k) \= t₁ \+ t₂ exp(ik) crosses zero, marking the topological phase boundary. Each pair of crossings (entry and exit of the D_e \< D_g regime) corresponds heuristically to one winding of the h(k) trajectory around the origin of the complex plane.

From this heuristic mapping, seeds 42 and 43 (4 crossings) yield winding number w \= 2, and seed 44 (2 crossings) yields w \= 1\. All three are consistent with non-trivial SSH topology (w ≥ 1). The outer crossing near r ≈ 2.4–2.6 is reproducible across all three seeds, suggesting a substrate-specific correlation length associated with the quasicrystalline long-range order.

| Seed | D_g | Δ \= D_e−D_g | Γ | Crossings | w (heuristic) | ρ^I |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **42** | 2.082 | −0.549 | 1.106 | 4 | **w \= 2** | 0.701 |
| **43** | 2.071 | −0.685 | 0.979 | 4 | **w \= 2** | 0.737 |
| **44** | 2.089 | −0.893 | 1.356 | 2 | **w \= 1** | 0.753 |

*Table 3\. Topological characterisation of Penrose full-evolution runs. Winding numbers are heuristic estimates from zero-crossing counts. Rigorous Bott index computation at N ≥ 5,000 is in preparation.*

## **4.4 The Bott Index: Status and Finite-Size Analysis**

The Bott index is the rigorous real-space topological invariant for non-periodic systems, including quasicrystals on S² (Hastings & Loring, 2011). For a projector P onto the occupied subspace of H:

B \= (1/2π) Im(Tr(log(U_x U^y U_x† U^y†)))

where U_x \= P exp(2πi X/L_x) P \+ (I−P) and similarly for U^y. B is integer-valued in the thermodynamic limit and equals the Chern number when translational symmetry holds.

At N \= 1,000, the Bott index returns B \= 0 for all three Penrose seeds. Subsequent dedicated spectral analysis of the gauge-coupled Peierls Hamiltonian, scanning the level spacing ratio \langle r\rangle across system sizes N \= 100–600, phason directions u, and coupling angles \theta, provides definitive resolution of this question without requiring larger-N computation.

The analysis reveals weak, broad modulations of P(critical) at intermediate N (peaks near N \≈ 140 and N \≈ 440 with P(critical) \≤ 0.3), but these fluctuations are not reproducible across phason angles and vanish in the large-N limit. At N \≥ 500, the system converges robustly to GOE statistics (\langle r\rangle \≈ 0.53). We conclude that the Peierls Hamiltonian of the Penrose CQFT substrate occupies the ergodic phase: quasiperiodic geometry induces transient scale-dependent spectral structure that renormalises to GOE universality, but no discrete scale invariance or persistent critical regime is observed.

This result revises the interpretation of the heuristic winding numbers w \= 1–2 and the elevated \rho^I. These quantities remain valid empirical measurements, but their explanation is not static eigenstate topological protection. Instead, they reflect the non-equilibrium routing capacity of the quasicrystalline substrate: the aperiodic bond structure sustains persistent circulating currents in the NESS without requiring a spectral gap. The transient spectral modulations at intermediate N are themselves a genuine geometric effect — absent in random and lattice null models — consistent with the quasicrystalline correlation structure, and reportable as such. The Bott index computation at N \≥ 5,000 is accordingly removed from the compute roadmap; those resources are redirected to the transformer inference analysis and NESS confirmation experiments (Section 6).

## **4.5 The Microtubule Connection**

Microtubules, the primary cytoskeletal filaments proposed as quantum computation substrates in Orchestrated Objective Reduction (Orch OR) theory, share three structural features with the Penrose quasicrystal simulated here: non-periodic long-range order along the protofilament axis (in humans: 13 protofilaments with a quasi-crystalline seam offset of 3/13 tubulin subunits), bimodal nearest-neighbour distance distribution (lateral and longitudinal tubulin contacts), and cylindrical quasi-1D topology supporting SSH-like protected boundary modes at the plus and minus ends.

Our CQFT framework provides a geometric selection rule — only substrates maintaining \Delta \< 0 and elevated \rho^I can sustain coherent non-equilibrium self-referential dynamics — that is structurally analogous to the routing capacity proposed in Orch OR theory. We note that the topological protection mechanism in Orch OR is typically invoked at the quantum level, whereas the present framework operates classically; the structural analogy is one of substrate geometry enabling persistent flow, not of quantum eigenstate protection. Whether microtubule geometry satisfies both criteria is a testable prediction, not a claimed result. We do not claim to have proven Orch OR or to have demonstrated quantum coherence in biological systems. The connection is a formal structural analogy that motivates future experimental work.

# **5\. Implications for AGI Safety Monitoring and Hardware Architecture**

## 

## **5.1 The Geometric Safety Monitoring Paradigm**

Current AI alignment approaches treat safety as a behavioural question: does the system produce harmful outputs? The CQFT framework proposes a complementary structural approach: does the system's internal geometric organisation indicate coherent, self-consistent dynamics? These questions are independent; a system may produce safe outputs while its internal geometry is misaligned, or vice versa. Early geometric warning may precede behavioural failure.

The key insight is that the metrics Γ, Δ(r), D_g, and ρ^I are computable from the internal activation graphs of transformer-based AI systems without model modification or retraining. The attention weight matrix W^{attn} of a transformer layer defines a weighted graph on the token sequence; the CQFT analysis pipeline (Grassberger-Procaccia estimator, correlation function G(r), Helmholtz decomposition) applies directly to this graph.

## **5.2 Five Falsifiable Predictions**

The following predictions are stated in advance and are testable on existing production models. Confirmation or refutation of any prediction constitutes meaningful evidence about the geometric coherence framework.

**Prediction 1\.**

The embedding gap Γ computed from transformer attention graphs is lower for coherent natural language inputs than for random token sequences on the same model. Operationalisation: compute Γ on 100 coherent prompts and 100 random token sequences of identical length; test H₀: Γ^{coh} \= Γ^{rand} paired by sequence length.

**Prediction 2\.**

The layer-wise gradient ∂Γ/∂l is negative on average during coherent inference: later layers show lower embedding gap than earlier layers. This would indicate progressive geometric self-organisation through the network depth, analogous to the order-increasing dynamics observed in the Penrose simulation.

**Prediction 3\.**

Models with rotary positional encoding (RoPE) or attention with linear biases (ALiBi) exhibit larger coherence gradients |∂Γ/∂l| than models with absolute positional embedding. RoPE and ALiBi encode relative position geometrically, potentially introducing a quasiperiodic structure into the attention graph that our framework predicts would be more conducive to self-organisation.

**Prediction 4 (Primary).**

The embedding gap Γ decreases monotonically with model scale from 125M to 70B parameters. This would constitute the first geometric coherence scaling law for AI systems, analogous to the empirical scaling laws for loss, compute, and parameters (Kaplan et al., 2020\) but measuring internal structural coherence rather than prediction accuracy.

**Prediction 5\.**

A non-monotone (“breathing”) Γ profile across layers is more pronounced on harder inference tasks (multi-step reasoning, code generation) than on simpler tasks (single-token completion). The breathing pattern would indicate the system alternately expanding and contracting its geometric coherence as it works through complex inference steps.

## **5.3 Hardware Architecture Implications**

The cubic lattice result, order gain \+0.001 versus \+0.188 for Penrose, a 165-fold suppression, has a direct implication for AI accelerator design. Current GPUs implement cubic lattice interconnect topology in their memory hierarchies and register file structures. Our data provide the first quantitative measurement of the dynamical suppression this architecture imposes on self-organising field dynamics.

This is not a software limitation. No algorithmic improvement can compensate for a 165-fold geometric suppression of self-organisation, because the suppression arises from the substrate topology itself, not from any particular operation performed on that substrate. The implication for neuromorphic hardware design is concrete: interconnect fabrics with quasicrystalline or quasi-periodic topology should exhibit substantially higher capacity for self-organising dynamics than cubic lattice designs.

The Volatco GA144 multi-computer architecture, with its irregular mesh connectivity, is a candidate for experimental evaluation against the Penrose topological standard. Mapping the GA144 connectivity graph to the CQFT substrate framework and measuring Γ, Δ(r), and ρ^I would provide the first empirical comparison between a commercially available neuromorphic architecture and the geometric substrate criterion established here.

# **6\. Way Forward: GPU Compute Roadmap**

## 

## **6.1 Priority 1 (Revised): NESS Confirmation — Loop Flux and Topological Lifetime (A100, \~4 hours)

The Bott index computation at N \= 5,000 is superseded by the spectral analysis result: the Peierls Hamiltonian converges to GOE universality at N \≥ 500, confirming B \= 0 as a physical result rather than a finite-size artifact. This priority is therefore reallocated to direct empirical confirmation of the NESS interpretation, which is the stronger and more novel claim.

Three decisive tests are planned: (i) loop flux measurement (mean |\Phi_{loop}| across simulation-edge triangles, quantifying persistent circulation); (ii) antisymmetric current persistence (time-averaged \langle J_{ij}\rangle_t \≠ 0, confirming broken detailed balance); and (iii) topological lifetime \Lambda = \tau_{topo}/\tau_{eq} from two-component autocorrelation fits. The prediction is \Lambda \gg 1 for Penrose, \Lambda \≈ 1 for cubic lattice — a directly falsifiable distinction between the NESS and equilibrium regimes. Total compute: approximately 4 A100-hours at N \= 1,000 across three geometries and three seeds.

## **6.2 Priority 2: N \= 10,000 Scaling Experiment (\~15 hours per geometry)**

The N \= 1,000 results establish qualitative trends. The N \= 10,000 experiment tests whether these trends persist at a larger scale and extracts the finite-size scaling exponents. Key questions: does D_g(Penrose) converge to a specific value as N increases? Does the zero-crossing structure of Δ(r) become sharper (suggesting approach to a genuine fixed point) or broader (suggesting no fixed point exists)?

Computationally: N \= 10,000 requires O(N²) adjacency operations per step, approximately 100× more expensive than N \= 1,000. At 12,000 steps this is approximately 15 hours per geometry on an A100, or 45 hours for the full three-geometry comparison. The ℏ-sweep (stochastic quantisation at four noise amplitudes) can be run in parallel on the same hardware.

## **6.3 Priority 3: Stochastic Quantisation ℏ-Sweep (\~8 hours)**

Replacing the fixed noise amplitude σ \= 0.02 with σ \= √(2ℏ/dt) and varying ℏ ∈ {0.001, 0.01, 0.1, 1.0} generates quantum-corrected versions of the classical dynamics. The key observable is the ℏ-dependence of the zero-crossing position r\*: if r\* is stable across ℏ values for Penrose geometry but shifts for random and lattice, this constitutes the topological protection hypothesis in quantitative form. Total compute: approximately 8 hours on an A100 for four ℏ values at N \= 1,000.

## 

## **6.4 Priority 4: Transformer Inference Geometric Analysis**

The five falsifiable predictions require computing Γ, Δ(r), and D_g from transformer attention graphs at multiple model scales. The measurement pipeline is:

* Extract attention weight matrices W^{attn} from each layer during inference (hooks, no gradient computation needed)

* Build weighted graph on token sequence using W^{attn} as adjacency weights

* Compute D_g via Grassberger-Procaccia on the token embedding positions

* Compute G(r) from cosine similarities between token embeddings at distance r in attention space

* Extract Δ(r) \= D_e(r) − D_g and Γ

Model scales: GPT-2 (117M, 345M, 762M, 1.5B) are freely available via Hugging Face and run on a single A100. LLaMA-2 (7B, 13B, 70B) require multi-GPU but are also available. The scaling law test (Prediction 4\) requires at minimum four points spanning one order of magnitude in parameter count; GPT-2 provides four points in a single GPU session (\~4 hours setup, ongoing).

## **6.5 Priority 5: Full Experimental Matrix at N \= 5,000 (\~90 hours)**

The complete 2×3 matrix at N \= 5,000 (three geometries × two modes × three seeds) replaces the current N \= 1,000 results with properly scaled data. At N \= 5,000, finite-size effects in D_g and ρ^I are substantially reduced, the Bott index is expected to be well-defined, and the zero-crossing structure of Δ(r) should be sharper. This is the definitive dataset for the publication.

Total GPU compute for Priority 5: approximately 90 A100-hours, feasible in a single NVIDIA Innovation Lab allocation. Combined with Priorities 1-4, the full scientific programme requires approximately 120 A100-hours.

| \# | Computation | A100-hrs | N | Key deliverable |
| :---: | :---: | :---: | :---: | :---: |
| **1** | NESS: loop flux + lifetime \Lambda (3 geoms \× 3 seeds) | \~4h | 1,000 | NESS confirmed/falsified |
| 2 | Full 3-geometry scaling | \~45h | 10,000 | Finite-size scaling exponents |
| 3 | ℏ-sweep (stochastic quantisation) | \~8h | 1,000 | Quantum corrections to Δ(r) |
| 4 | Transformer inference analysis | \~4h | N/A | Scaling law for Γ vs. model size |
| 5 | Full matrix at N=5,000 | \~90h | 5,000 | Definitive publication dataset |
|  | TOTAL | \~153h |  | **Experiment concluded**  |

*Table 4\. GPU compute roadmap. All items feasible within a single NVIDIA Innovation Lab DGX Cloud allocation.*

# **7\. Conclusion**

We have demonstrated, through a controlled 12-condition computational experiment, that substrate geometry is the primary determinant of self-organisational capacity in co-evolutionary field-geometry dynamics. The Penrose icosahedral quasicrystal produces a 165-fold higher order gain than the cubic lattice, a reproducible geometry-dominated signed embedding gap Δ \= −0.709 ± 0.141, a 3.4× gap reduction by the geometry update rule, and a consistently elevated Helmholtz rotational fraction ρ^I \= 0.730 ± 0.022 \- all across three independent random seeds.

These results establish three convergent empirical criteria for substrate-dependent coherence (consistent Δ \< 0, substantial order gain, elevated ρ^I) and provide the first quantitative substrate-selection criterion distinguishing quasicrystalline from cubic lattice geometry. Structural isomorphism with the SSH topological insulator model is formally motivated; rigorous confirmation via the Bott index at N ≥ 5,000 is the next computational priority.

The implications are three-fold. For AGI safety: five falsifiable predictions are stated in advance, testable on existing production AI systems without model modification. For hardware architecture: the cubic lattice substrate of current GPUs imposes a quantified 165-fold suppression of self-organisational dynamics, motivating quasicrystalline interconnect design as a hardware-level safety criterion. For fundamental theory: the ouroboros conjecture, that a self-referential field spontaneously selects its own geometrically self-consistent substrate, survives as a falsifiable hypothesis. The Penrose quasicrystal is the candidate substrate not because its eigenspectrum is topologically non-trivial — spectral analysis shows it is not, at accessible N — but because its aperiodic routing topology sustains the non-equilibrium steady state in which self-referential dynamics can persist. The fixed point \Delta \= 0 remains a theoretical target; the NESS regime \Delta \< 0 with elevated \rho^I is the empirically confirmed precondition.

The question is no longer whether substrate geometry constrains field coherence. The data show that it does. The question is whether we will measure it in deployed AI systems before, rather than after, the consequences of geometric misalignment become visible in behaviour.

**Acknowledgements**

Computations were performed on Google Colab with Drive-backed persistent storage. The author thanks the open-source scientific Python ecosystem (NumPy, SciPy, Matplotlib). NVIDIA Innovation Lab compute access is pending for the N ≥ 5,000 programme.

# **References**

Hastings, M.B. & Loring, T.A. (2011). Topological insulators and C\*-algebras: Theory and numerical practice. Annals of Physics, 326(7), 1699–1727.

Hameroff, S. & Penrose, R. (2014). Consciousness in the universe: A review of the ‘Orch OR’ theory. Physics of Life Reviews, 11(1), 39–78.

Kaplan, J., McCandlish, S., Henighan, T., et al. (2020). Scaling laws for neural language models. arXiv:2001.08361.

Penrose, R. (1974). The role of aesthetics in pure and applied mathematical research. Bulletin of the Institute of Mathematics and its Applications, 10, 266–271.

Parisi, G. & Wu, Y.S. (1981). Perturbation theory without gauge fixing. Scientia Sinica, 24(4), 483–496.

Su, W.P., Schrieffer, J.R. & Heeger, A.J. (1979). Solitons in polyacetylene. Physical Review Letters, 42(25), 1698–1701.
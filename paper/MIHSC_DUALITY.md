# Quantised Inertia as an Effective Description of OPH

## The MiHsC/OPH IR Duality

McCulloch's Quantised Inertia (MiHsC) and Observer Patch Holography (OPH) both produce the acceleration scale $a_0 \sim c^2/R_H$ and the same galaxy phenomenology (flat rotation curves, baryonic Tully-Fisher, radial acceleration relation) without dark matter particles. MiHsC modifies inertia; OPH modifies gravity. In the Newtonian limit these are equivalent to leading order. They diverge on gravitational lensing and redshift evolution of $a_0$.

---

# 1. MiHsC in Equations

## 1.1 Assumptions

**M1 (Unruh origin of inertia).** Inertial mass arises from momentum carried by Unruh radiation. An observer with proper acceleration $a$ sees a thermal bath at:

$$T_U = \frac{\hbar a}{2\pi c k_B}$$

with characteristic wavelength $\lambda_U \sim c^2/a$.

**M2 (Cosmic mode suppression).** Unruh modes with $\lambda_U > \Theta$ (cosmic horizon diameter, $\Theta \approx 2R_H$) are disallowed. Fraction of permitted modes: $f(a) = 1 - \lambda_U/\Theta$.

## 1.2 Modified Inertial Mass

$$\boxed{m_i = m_g \left(1 - \frac{2c^2}{|a| \, \Theta}\right)}$$

Standard physics at $|a| \gg 2c^2/\Theta$. Inertia vanishes at $a_{\min} = 2c^2/\Theta$.

## 1.3 Galaxy Dynamics

Circular orbit with modified inertia:

$$m_g \left(1 - \frac{2c^2}{a\Theta}\right) a = \frac{G m_g M_b}{r^2}$$

Deep-MOND regime ($a \to a_{\min}$):

$$a^2 \approx \frac{2c^2}{\Theta} \cdot \frac{G M_b}{r^2} \quad \Rightarrow \quad \boxed{v^4 \approx \frac{2 G M_b c^2}{\Theta}}$$

This is Tully-Fisher with $a_0^{(\text{MiHsC})} = 2c^2/\Theta$.

---

# 2. OPH IR Structure (Review)

All results from the main paper (Section 5.15) and technical supplement (Sections 8-9).

## 2.1 Screen Capacity to $\Lambda$

$\Lambda$ is undetermined by local null modular data. It requires a global input:

$$\Lambda = \frac{3\pi}{G \cdot \log(\dim \mathcal{H}_{\text{tot}})}, \quad r_{dS} = \sqrt{\frac{3}{\Lambda}} \approx 1.66 \times 10^{26} \text{ m}$$

## 2.2 Modular Anomaly

The collar modular additivity defect:

$$\Delta K_\delta := K_{ABD} - K_{AB} - K_{BD} + K_B, \quad \langle \Delta K_\delta \rangle_\omega = -I(A:D|B)_\omega$$

modifies Einstein's equation:

$$G_{ab} + \Lambda g_{ab} = 8\pi G \left(\langle T_{ab} \rangle + \langle T_{ab}^{\text{anom}} \rangle\right)$$

$$\langle T_{00}^{\text{anom}} \rangle = \frac{15}{8\pi^2} \cdot \frac{\delta \langle K_C^{(\text{anom})} \rangle}{\ell^4}$$

The coefficient $15/(8\pi^2)$ comes from inverting the $d=4$ geometric factor $\Omega_2/(4^2-1) = 4\pi/15$.

## 2.3 MOND Acceleration Scale

The IR modification must vanish if $r_{dS} \to \infty$, be controlled by $r_{dS}$ alone, and carry the non-tunable $15/(8\pi^2)$. This fixes:

$$\boxed{a_0^{(\text{OPH})} = \frac{15}{8\pi^2} \cdot \frac{c^2}{r_{dS}} \approx 1.03 \times 10^{-10} \text{ m/s}^2}$$

Observed: $a_0 \approx 1.2 \times 10^{-10}$ m/s$^2$ (within 15%).

## 2.4 Galaxy Phenomenology

Deep-IR polarization response (Technical Supplement, Section 9.5):

$$S_{\text{pol}}[\varphi] = \int d^3x \left[-\frac{1}{12\pi G a_0}|\nabla\varphi|^3 - \rho_b \varphi\right]$$

yields:

$$g_{\text{obs}} \approx g_b + \sqrt{a_0 \cdot g_b}$$

Tully-Fisher: $V^4 \approx G M_b \, a_0^{(\text{OPH})}$. Flat rotation curves: $M_{\text{DM}}(r) \propto r$.

---

# 3. The Structural Mapping

## 3.1 Correspondence

| | MiHsC | OPH |
|-|-------|-----|
| **IR scale** | Horizon diameter $\Theta$ | de Sitter radius $r_{dS}$ |
| **Origin** | Cosmological input | Derived: $\Lambda = 3\pi/(G \log \dim \mathcal{H}_{\text{tot}})$ |
| **Mechanism** | Unruh mode suppression | Modular anomaly from finite screen capacity |
| **What is modified** | Inertial mass: $m_i = m_g(1 - 2c^2/a\Theta)$ | Gravitational source: $T_{ab} \to T_{ab} + T_{ab}^{\text{anom}}$ |
| **Where $a_0$ lives** | Inertia sector | Gravity sector |
| **Scale** | $a_0 = 2c^2/\Theta$ | $a_0 = (15/8\pi^2) c^2/r_{dS}$ |
| **Unruh effect** | Assumed | Derived (geometric modular flow) |

Both share the logical skeleton:

```
Finite cosmic boundary --> IR constraint --> modified low-acceleration dynamics
    --> a_0 ~ c^2/R_cosmic --> galaxy phenomenology without dark matter
```

## 3.2 Dimensional Universality

**Proposition 3.1.** Any framework that (a) modifies gravity or inertia in the IR, (b) has a single cosmic length scale $R$, and (c) produces acceleration-scale effects, gives $a_0 \sim c^2/R$ by dimensional analysis. The nontrivial content is in the prefactors and mechanism.

## 3.3 Prefactors

OPH: $15/(8\pi^2) \approx 0.190$, derived from $d=4$ geometry, non-tunable.

MiHsC: factor of 2 from Wien displacement law; depends on spectral peak choice and horizon identification. $O(1)$ ambiguity.

Numerically: $a_0^{(\text{OPH})} \approx 1.03 \times 10^{-10}$ m/s$^2$ vs $a_0^{(\text{MiHsC})} \approx 6.9 \times 10^{-10}$ m/s$^2$ (using $\Theta = 8.8 \times 10^{26}$ m). OPH is within 15% of the observed value; MiHsC overshoots by a factor of ~6 unless the horizon identification is revised.

---

# 4. Newtonian Equivalence

MiHsC modifies $m_i$ (left side of $F=ma$). OPH modifies the gravitational source (right side of Einstein's equation). These are equivalent to leading order.

**Proposition 4.1.** Modified inertia $m_i = m_g(1-\epsilon)$ with $\epsilon \ll 1$ is equivalent to additional gravitational acceleration $g_{\text{anom}} = \epsilon \, g_b$.

*Proof.* From $m_i a = m_g g_b$:

$$a = \frac{g_b}{1-\epsilon} = g_b + \epsilon g_b + O(\epsilon^2)$$

Compare OPH: $g_{\text{obs}} = g_b + g_{\text{anom}}$. Identification: $g_{\text{anom}} = \epsilon g_b$. $\square$

In MiHsC, $\epsilon = 2c^2/(|a|\Theta)$. In the deep-MOND limit ($a \sim \sqrt{a_0 g_b}$) this gives $g_{\text{anom}} \sim \sqrt{a_0 g_b}$, the same RAR form as OPH.

---

# 5. Does OPH Subsume MiHsC?

OPH derives what MiHsC assumes:

- **Unruh effect:** OPH derives it from geometric modular flow (Theorem 2.2). MiHsC takes it as given.
- **Mode suppression:** MiHsC postulates a hard wall at $\Theta$. OPH has finite screen capacity ($\log \dim \mathcal{H}_{\text{tot}} < \infty$), which implies that modes with $\lambda \gtrsim r_{dS}$ cannot be encoded. The hard wall is a phenomenological proxy for finite Hilbert space dimension.

Where subsumption is incomplete:

1. MiHsC predicts a hard $a_{\min} = 2c^2/\Theta$. OPH's anomaly is smooth.
2. MiHsC ties suppression to each object's Rindler horizon. OPH's boundary is the global de Sitter screen.
3. MiHsC identifies inertia with Unruh radiation pressure. OPH derives inertia from full overlap consistency.

---

# 6. Testable Divergences

## 6.1 Gravitational Lensing

Modified inertia (MiHsC) does not modify spacetime curvature: lensing traces baryonic mass only. Anomalous stress-energy (OPH) curves spacetime: lensing includes the dark component.

| | MiHsC | OPH |
|-|-------|-----|
| Lensing | Baryonic mass only | Baryonic + anomalous |

Bullet Cluster lensing data show lensing offset from baryonic mass, favouring OPH.

## 6.2 Redshift Evolution

MiHsC: $a_0(z) = 2c^2/\Theta(z)$, where $\Theta$ grows with cosmic time. $a_0$ was larger in the past.

OPH: $a_0 = (15/8\pi^2) c^2 \sqrt{\Lambda/3}$. Constant if $\Lambda$ is constant.

Testable with high-$z$ galaxy kinematics (e.g., JWST at $z > 2$).

## 6.3 Summary

| Test | MiHsC | OPH | Current evidence |
|------|-------|-----|-----------------|
| Lensing | Baryons only | Includes anomaly | Favours OPH |
| $a_0(z)$ | $\propto 1/\Theta(t)$ | const | Insufficient data |
| $a_0$ value | $\sim 6.9 \times 10^{-10}$ | $\approx 1.03 \times 10^{-10}$ | Observed $\approx 1.2 \times 10^{-10}$ |
| Clusters | Same scaling | Environment-dependent | Clusters need more |

---

# 7. Status

| Claim | Status |
|-------|--------|
| Both produce $a_0 \sim c^2/R_{\text{cosmic}}$ | Verified (dimensional analysis) |
| Newtonian-regime equivalence | Proven (Proposition 4.1) |
| OPH derives Unruh effect that MiHsC assumes | Derived (Theorem 2.2) |
| OPH $a_0$ prefactor non-tunable | Derived ($d=4$ geometry) |
| MiHsC is effective IR description of OPH | Conjectured |
| Lensing distinguishes the two | Plausible; needs full relativistic treatment |
| Rigorous mode-suppression-from-capacity derivation | Open |

---

## References

1. McCulloch, M. E. (2007). "Modelling the Pioneer anomaly as modified inertia." MNRAS 376, 338-342.
2. McCulloch, M. E. (2017). "Galaxy rotations from quantised inertia and visible matter only." Astrophys. Space Sci. 362, 149.
3. Renda, M. (2019). "A sceptical analysis of quantised inertia." MNRAS 489, 881-885.
4. Milgrom, M. (1983). "A modification of the Newtonian dynamics." ApJ 270, 365-370.
5. McGaugh, S. S. et al. (2016). "Radial acceleration relation in rotationally supported galaxies." PRL 117, 201101.
6. Unruh, W. G. (1976). "Notes on black-hole evaporation." Phys. Rev. D 14, 870.
7. Jacobson, T. (1995). "Thermodynamics of spacetime." PRL 75, 1260.

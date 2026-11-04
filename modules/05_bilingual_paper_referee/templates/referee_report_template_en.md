# Confidential Peer Review Report (English)
# Target Venue: Journal of Biomechanics / IEEE Transactions on Biomedical Engineering

**Manuscript Reference:** [JB-2026-0319]  
**Manuscript Title:** [Adaptive Quasi-Stiffness Knee Exoskeleton Modulates Lower-Limb Joint Moments in Post-Stroke Locomotion]  
**Reviewer:** [Peer Reviewer Specialist in Biomechanics]  
**Date of Review:** [YYYY-MM-DD]  
**Recommendation:** [Major Revision]  

---

## 1. Executive Summary & Overview
This manuscript evaluates the biomechanical efficacy of an active quasi-stiffness knee exoskeleton in modulating sagittal knee moments and surface EMG activation profiles across ten chronic post-stroke individuals during treadmill walking. Synchronized 3D motion capture and split-belt instrumented treadmill data were analyzed via recursive inverse dynamics. The clinical objective and the engineering design are of genuine interest to the biomechanics community. However, several critical methodological concerns regarding filtering frequency discrepancy, EMG normalization protocols, and unaddressed soft-tissue artifact (STA) preclude acceptance in its present form. Detailed major and minor comments are provided below to guide the authors during revision.

---

## 2. Key Strengths
1. Direct experimental validation on a clinical patient population rather than relying purely on healthy surrogate simulations.
2. Synchronized multi-modal data acquisition combining optoelectronic motion capture, ground reaction forces, and multi-channel sEMG.
3. Logical introduction with an empirical justification of mechanical work reduction in hemiparetic gait.

---

## 3. Major Revisions (Required for Reconsideration)

1. **Discrepancy in Kinematic vs. Kinetic Cutoff Frequencies (Section 2.3, Line 114):**  
   The authors filtered 3D marker trajectories with a low-pass Butterworth filter at 6 Hz while filtering force plate data at 25 Hz. It is a well-established principle in inverse dynamics (e.g., Bisseling & Hof, 2006; Winter, 2009) that filtering kinematics at a lower frequency than kinetics introduces severe artificial acceleration artifacts and non-physical force spikes near heel-strike. The authors must reprocess their joint moment calculations using matched cutoff frequencies determined via residual analysis or justify the choice with a sensitivity analysis.

2. **Unnormalized Surface EMG Amplitudes (Section 2.4, Lines 142–148):**  
   The authors present rectus femoris and biceps femoris EMG linear envelopes in raw millivolts ($mV$) when comparing the baseline unassisted condition against the assisted exoskeleton condition across participants. Inter-individual variations in skin impedance, subcutaneous adipose tissue, and electrode re-application render raw amplitude comparisons invalid. The authors must normalize their EMG signals to maximal voluntary isometric contractions (% MVC) or dynamic functional peak envelopes.

3. **Sample Size Justification & Power Analysis (Section 2.5):**  
   The cohort consists of $n=10$ hemiparetic participants. Was an a priori power calculation performed? Given the high inter-subject variability inherent to stroke gait, please report effect sizes (e.g., Cohen's $d_z$ or partial $\eta^2$) and $95\%$ confidence intervals alongside exact $p$-values. Furthermore, with multiple paired comparisons across phases, a Bonferroni or Holm-Sidak correction is required to control family-wise Type I error.

4. **Soft Tissue Artifact (STA) Consideration (Section 4):**  
   The thigh and shank marker clusters are mounted on external exoskeleton cuffs. The relative displacement between the exoskeleton frame, the limb soft tissue, and the underlying femur/tibia was not measured or discussed. The authors must explicitly quantify or discuss the magnitude of STA and cuff migration as a limitation in the Discussion.

---

## 4. Minor Comments & Editorial Corrections

1. **Line 18 (Abstract):** The term `"proves the unquestionable superiority"` is overstated. Replace with empirical, measured phrasing such as `"demonstrated an 18.4% reduction in peak knee extensor moment"`.
2. **Table 1:** The table contains multiple vertical borders, violating the standard 3-rule booktabs format. Please remove all vertical grid lines and present the data using top, middle, and bottom horizontal rules only.
3. **Figure 3:** Please add an explicit vertical dashed line indicating toe-off ($\approx 60\%$ gait cycle) and define the shaded area as $\pm 1$ standard deviation in the figure caption.
4. **Units Formatting:** In Section 3.2, joint moments are written as `Nm/kg`. Standard SI typography requires a middle dot: `N·m/kg`.
5. **Reference Formatting:** Reference 14 (Wu et al., 2002) lacks the full volume and page numbers. Please update according to journal style.

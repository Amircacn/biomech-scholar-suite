# Biomechanics Laboratory Report: Lower-Extremity Kinematic and Kinetic Analysis during Normal Human Gait

**Experiment:** 3D Motion Capture and Ground Reaction Force Analysis in Level Walking  
**Author:** [Student Name] | **Student ID:** [12345678]  
**Department:** Department of Biomedical Engineering (Biomechanics Division)  
**Instructor:** Prof. [Instructor Name]  
**Date of Execution:** [YYYY-MM-DD] | **Date of Submission:** [YYYY-MM-DD]  

---

## 1. Executive Summary
This laboratory study evaluated sagittal-plane knee kinematics and net internal joint moments during level walking across a single healthy participant (male, 24 years, mass: 74.2 kg, height: 1.78 m). Experimental data were collected synchronously using a 10-camera infrared optoelectronic motion capture system (100 Hz) and dual multi-axis force platforms (1000 Hz). The results showed a peak loading-response knee flexion of $19.2^\circ \pm 2.4^\circ$, followed by a swing-phase peak flexion of $61.5^\circ \pm 3.1^\circ$. The maximum internal knee extension moment reached $1.28 \pm 0.14\text{ N}\cdot\text{m/kg}$ during early stance, providing dynamic joint stabilization against the external flexion moment. The kinematic and kinetic profiles demonstrated high congruence with canonical normative datasets, confirming physiological knee joint mechanics.

---

## 2. Theoretical Background and Governing Formulations
Inter-segmental forces and net internal joint moments are computed via recursive Newton-Euler inverse dynamics formulated in a bottom-up sequence:

$$\sum \vec{F} = m \cdot \vec{a}_{COM} \implies \vec{F}_{\text{proximal}} = m (\vec{a}_{COM} - \vec{g}) - \vec{F}_{\text{distal}}$$

$$\sum \vec{M}_{COM} = \dot{\vec{H}} = \mathbf{I} \cdot \vec{\alpha} + \vec{\omega} \times (\mathbf{I} \cdot \vec{\omega})$$

where $m$ denotes segmental mass, $\vec{a}_{COM}$ is linear acceleration of the segment center of mass, $\vec{g}$ is gravitational acceleration, $\mathbf{I}$ represents the 3D mass moment of inertia tensor, and $\vec{\omega}, \vec{\alpha}$ correspond to angular velocity and angular acceleration vectors, respectively. Cardan/Euler angle decomposition follows the standard $Z-X-Y$ sequence recommended by the International Society of Biomechanics (ISB).

---

## 3. Apparatus and Participant Specifications

### 3.1. Anthropometrics
- Age: 24 yrs | Height: 1.78 m | Body Mass: 74.2 kg | Shank Length: 43.5 cm | Knee Diameter: 9.8 cm

### 3.2. Instrumentation Configuration
1. **Optoelectronic Motion Capture (Vicon):** 10 infrared cameras operating at 100 Hz; spatial reconstruction residual $< 0.15\text{ mm}$.
2. **Piezoelectric Force Platforms (Kistler Type 9281EA):** Dimensions 400 × 600 mm, sampled at 1000 Hz, linearity error $< 0.2\%$.
3. **Retroreflective Marker Set:** Standard Plug-in Gait Lower-Body protocol comprising 16 spherical retroreflective markers (14 mm diameter).

---

## 4. Experimental Protocol
1. **Static Trial & Skeletal Calibration:** The participant assumed an anatomical standing posture centered on the force platform to calibrate segmental coordinate frames and joint center locations.
2. **Dynamic Walking Trials:** The subject traversed a 10-meter walkway at self-selected comfortable gait velocity ($1.35 \pm 0.08\text{ m/s}$). Five clean foot strikes completely contained within the boundary of the force plates were captured. A 2-minute rest interval separated consecutive trials to prevent neuromuscular fatigue.

---

## 5. Signal Conditioning and Data Processing
- **Kinematic Filtering:** 3D marker coordinates were conditioned using a 4th-order zero-lag low-pass Butterworth filter with a 6 Hz cutoff frequency, determined via Jackson and Winter residual analyses.
- **Kinetic Filtering:** Raw ground reaction forces were low-pass filtered at 10 Hz to eliminate impact spikes while preserving peak kinetic values.
- **Gait Cycle Normalization:** Consecutive heel-strike events ($t_0$ to $t_{100}$) were identified from vertical force thresholds ($F_z > 20\text{ N}$) and time-normalized across 101 discrete points (0% to 100% gait cycle) via cubic spline interpolation.

---

## 6. Results

### Table 1: Sagittal knee kinematic and kinetic parameters during gait phases
| Biomechanical Parameter | Measured Value (Mean ± SD) | Literature Normative (Winter, 2009) | Unit |
|---|:---:|:---:|:---:|
| Knee Flexion at Heel-Strike | 4.2 ± 1.1 | 3.0 to 5.0 | deg |
| Peak Loading Response Knee Flexion | 19.2 ± 2.4 | 15.0 to 20.0 | deg |
| Peak Swing Phase Knee Flexion | 61.5 ± 3.1 | 58.0 to 65.0 | deg |
| Peak Vertical GRF (Loading Response) | 1.15 ± 0.06 | 1.10 to 1.20 | $BW$ |
| Peak Internal Knee Extension Moment | 1.28 ± 0.14 | 1.10 to 1.35 | $N\cdot m/kg$ |

*(Vector graphic plots with standard deviation confidence ribbons are archived in `04_figures/`).*

---

## 7. Error and Uncertainty Analysis
1. **Instrumentation Noise:** Spatial reconstruction residual of $\pm 0.15\text{ mm}$ contributes an estimated joint angle error of $< 0.3^\circ$.
2. **Soft Tissue Artifact (STA):** Relative skin motion over underlying skeletal landmarks represents the dominant error source, producing an estimated $1.5^\circ - 2.5^\circ$ kinematic uncertainty in non-sagittal planes.
3. **Body Segment Inertial Parameters (BSIP):** Regression equations based on Dempster cadavre tables introduce an estimated $\approx 8\%$ uncertainty in swing-phase dynamic moment peaks.

---

## 8. Discussion
The experimental findings confirm appropriate shock attenuation via controlled knee flexion during loading response, driven by eccentric quadriceps action. The calculated internal extension moment ($1.28\text{ N}\cdot\text{m/kg}$) counteracts the ground reaction force vector passing posterior to the knee joint center, preventing forward collapse. The observed trajectory matches canonical literature norms, validating the experimental protocol and processing pipeline.

---

## 9. References
1. Winter, D. A. (2009). *Biomechanics and Motor Control of Human Movement* (4th ed.). John Wiley & Sons. DOI: 10.1002/9780470549148
2. Perry, J., & Burnfield, J. M. (2010). *Gait Analysis: Normal and Pathological Function* (2nd ed.). SLACK Incorporated.
3. Robertson, D. G. E., et al. (2013). *Research Methods in Biomechanics* (2nd ed.). Human Kinetics.

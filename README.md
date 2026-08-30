# 🚀 AstroSense | AI Space Weather & Launch Risk Predictor

> Built for the **IBM SkillsBuild August Challenge 2026: Advance Space Exploration with AI** > Powered by **IBM Bob** | Integrated with Live **NASA DONKI Telemetry**

AstroSense is a real-time, AI-driven mission-control dashboard that transforms complex space weather telemetry into clear, actionable launch safety decisions. By ingesting live space weather data directly from NASA's DONKI API, AstroSense evaluates orbital radiation risks and provides real-time Go / No-Go launch assessments for mission operators.

---

## 🎯 Problem Statement
Space exploration operates in high-stakes environments where decision-making must be precise, data-rich, and time-sensitive. Solar flares, coronal mass ejections (CMEs), and geomagnetic storms directly threaten spacecraft avionics, satellite communications, and orbital safety. 

Traditional raw telemetry streams are data-heavy and difficult to parse under tight launch-window deadlines. AstroSense bridges this gap by converting complex space weather parameters into an intuitive risk trajectory and plain-English AI decision briefs.

---

## 💡 Key Features & Architecture
* **Live NASA Telemetry Ingestion:** Syncs directly with NASA DONKI API (`FLR`, `GST`, `SEP` endpoints) to track Solar Flare Intensity, Geomagnetic $Kp$-Index, Solar Wind Velocity, and Proton Radiation Flux.
* **24-Hour Predictive Risk Curve:** Interactive trajectory visualizer categorizing orbital safety into GO, CAUTION, and NO-GO safety thresholds.
* **IBM Bob AI Mission Specialist Widget:** Automated co-pilot that synthesizes multi-source metrics into real-time operational briefs and action plans for flight dynamics teams.
* **Space-Grade UI/UX:** Responsive dark-mode interface built with glassmorphism design principles tailored for ground control environments.

```text
[ NASA DONKI API ] ──(REST API)──> [ data_fetcher.py ] 
                                          │
                                   (Telemetry Feed)
                                          ▼
[ IBM Bob Specialist ] <──────────> [ app.py (Streamlit UI) ]
   (ai_specialist.py)                  │
                                (Interactive Plotly)
                                          ▼
                               [ Mission Control UI ]
                               
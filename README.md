# HydroBot 🌊🤖  
AI-Powered Solar Autonomous Surface Water Waste Collection Robot

HydroBot is an AI-driven, solar-powered autonomous surface water waste collection system designed for lakes, ponds, campus water bodies, and other small community-scale aquatic environments. The system combines real-time computer vision, autonomous navigation, a physical waste collection mechanism, and IoT-based environmental monitoring into a single modular robotic platform.

---

## Project Overview

Floating plastic waste and debris pose serious threats to aquatic ecosystems, especially in small and stagnant water bodies that are often neglected by large-scale cleanup solutions. HydroBot addresses this gap by providing a low-cost, intelligent, and sustainable robotic solution capable of detecting, navigating toward, and collecting surface-level waste autonomously.

HydroBot is designed as an **experimental learning and research-oriented prototype**, with emphasis on:
- Environmental impact
- Engineering modularity
- AI-driven decision making
- Renewable energy integration

---

## Key Capabilities

- AI-based detection of floating waste using YOLOv8
- Autonomous navigation using differential propulsion
- Physical surface waste collection using an intake mechanism
- Solar-powered hybrid energy system for long-duration operation
- Ultrasonic obstacle avoidance
- IoT-based real-time data logging and visualization
- Modular PVC catamaran design for stability and low cost

---

## System Architecture

HydroBot follows a perception → decision → action loop:

1. Camera captures live video feed
2. YOLOv8 performs real-time waste detection
3. Decision engine determines navigation commands
4. Motors steer the catamaran toward the target
5. Intake mechanism collects the waste
6. System updates waste count and sensor data to IoT dashboard
7. Robot returns to patrol mode

## Repository Structure

hydrobot/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── docs/
│   ├── system-overview.md
│   ├── process-map.md
│   ├── ai-pipeline.md
│   ├── power-management.md
│   ├── iot-dashboard.md
│   └── limitations-and-future-work.md
│
├── hardware/
│   ├── components-list.md
│   ├── mechanical-overview.md
│   └── wiring-overview.md
│
├── src/
│   ├── main.py
│   ├── config.py
│   │
│   ├── vision/
│   │   └── yolov8_inference.py
│   │
│   ├── navigation/
│   │   └── motor_control.py
│   │
│   ├── collection/
│   │   └── intake_control.py
│   │
│   └── sensors/
│       └── ultrasonic.py
│
├── iot/
│   └── data_publisher.py
│
├── tests/
│   └── motor_smoothing_test.py
│
└── assets/
    └── demo.gif

---

## Hardware Platform (High-Level)

- Raspberry Pi (AI inference and decision layer)
- Arduino UNO (motor and sensor control)
- Dual DC motors with motor driver
- Ultrasonic sensors for obstacle avoidance
- Solar panel with charge controller
- Li-ion battery system
- PVC twin-hull (catamaran) floating structure
- Waste collection basket / net mechanism

---

## Installation & Setup (Reference)

> This repository provides a reference implementation for academic and experimental use.

```bash
git clone https://github.com/your-username/hydrobot-ai-surface-waste-cleaner.git
cd hydrobot
pip install -r requirements.txt
python src/main.py
```
## This repository:

Demonstrates system architecture and control logic
Is intended for learning, research, and prototyping

## Team & Acknowledgements

Developed as part of an Experimental Learning Project (ELP).
Guided by academic supervision and inspired by sustainable development goals (SDG 14 – Life Below Water).

## Contact

For academic or collaboration-related queries, please open an issue in the repository.

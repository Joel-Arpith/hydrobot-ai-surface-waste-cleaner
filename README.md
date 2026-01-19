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

---

## Repository Structure


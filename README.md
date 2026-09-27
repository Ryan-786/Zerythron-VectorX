<div align="center">

# Zerythron Vector-X 🚁🤖
### Autonomous Heterogeneous Parent-Child UAV Swarm Framework
**Team ID:** `ZVX-GC1-2026` | **Track:** GC-1 · UAV-X: Resilient BVLOS Swarm Challenge  
**Organization:** ZERYTHRON PRIVATE LIMITED  

---

<!-- Tech Stack Badges / Logos -->
<p>
  <img src="https://img.shields.io/badge/ROS2-Humble_Hawksbill-22314E?style=for-the-badge&logo=ros&logoColor=white" alt="ROS 2">
  <img src="https://img.shields.io/badge/PX4-Autopilot_SITL-002B49?style=for-the-badge&logo=drone&logoColor=white" alt="PX4">
  <img src="https://img.shields.io/badge/Gazebo-Fortress-41505A?style=for-the-badge&logo=gazebo&logoColor=white" alt="Gazebo">
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/C++-17-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/OpenCV-Edge_Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/MANET-OLSRv2_Mesh-FF6F00?style=for-the-badge&logo=wifi&logoColor=white" alt="MANET">
</p>

</div>

---

## 📋 Table of Contents
1. [System Overview & Mission Objectives](#-system-overview--mission-objectives)
2. [Parent-Child Deployment & Operational Workflow](#-parent-child-deployment--operational-workflow)
3. [Complete Repository Structure](#-complete-repository-structure)
4. [Software Architecture & Core Modules](#-software-architecture--core-modules)
5. [Installation & Execution Instructions](#️-installation--execution-instructions)
6. [Technology Stack](#-technology-stack)

---

## 🌟 System Overview & Mission Objectives

**Zerythron Vector-X** is an advanced autonomous heterogeneous swarm architecture engineered specifically for Beyond Visual Line of Sight (BVLOS) disaster-response and defense scenarios. The system is designed to operate seamlessly in heavily obstructed, communication-denied environments where traditional Global Navigation Satellite Systems (GNSS) and infrastructure-backed wireless networks are severely jammed or destroyed.

### Key Innovations:
* **Heterogeneous Swarm Hierarchy:** Combines a high-altitude heavy-lift Parent carrier drone with agile, palm-sized Child micro-UAVs.
* **Decentralized Task Allocation:** Utilizes a custom implementation of Consensus-Based Bundle Algorithms (CBBA) for dynamic, conflict-free target assignment.
* **Resilient MANET Communications:** Integrates multi-hop ad-hoc mesh routing to maintain uninterrupted data transmission across deep-penetration missions.

---

## 🦅 Parent-Child Deployment & Operational Workflow

Traditional homogeneous swarm architectures suffer from restricted operational ranges and high susceptibility to communication link degradation when launched directly from ground control stations. Zerythron Vector-X resolves this bottleneck through a multi-stage aerial deployment sequence:

```text
[ Ground Control Station (GCS) ]
              │
              ▼ (Encrypted Long-Range Uplink)
[ Parent Carrier UAV (High-Altitude Overseer) ] 
              │
              ├──► High-Altitude Overhead Optical/LiDAR Mapping
              ├──► Hazard-Free "Clean Entry Corridor" Identification
              │
              ▼ (Deploys at Sector Perimeter)
[ Child UAV Swarm (4 Distributed Independent Nodes) ]
              │
              ├──► Autonomous Decentralized CBBA Auction & Coordination
              ├──► Edge AI Real-Time Survivor & Obstacle Detection
              └──► Multi-Hop MANET Mesh Relay ──► [ Safe Telemetry Stream back to GCS ]

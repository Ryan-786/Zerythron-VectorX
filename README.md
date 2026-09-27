# Zerythron Vector-X 🚀
### UAV-X: Resilient BVLOS Swarm Challenge (Team ID: `ZVX-GC1-2026`)
**Organization:** ZERYTHRON PRIVATE LIMITED  
**Track:** GC-1 · UAV-X: Resilient BVLOS Swarm Challenge  

---

## 🌟 Project Overview
**Zerythron Vector-X** ek advanced autonomous heterogeneous swarm architecture hai jo disaster-response aur defense operations ke liye design ki gayi hai jahan communication infrastructure completely damaged ya jammed hoti hai. Yeh system **Parent-Child Deployment Concept**, decentralized **Consensus-Based Task Allocation (CBBA)**, edge AI perception, aur resilient **MANET multi-hop mesh networking** ko ek sath integrate karta hai.

---

## 🦅 Parent-Child Deployment & Mission Concept
Traditional swarms ko ground se launch karne mein range aur communication loss ki problem aati hai. Hamara system isko is tarah solve karta hai:

1. **Parent UAV (High-Altitude Overseer):**
   * Ek heavy-lift carrier drone jo disaster zone ke upar high altitude par fly karta hai.
   * Wide-angle perception aur onboard mapping ke zariye debris aur obstacles ko scan karke ek safe **"Clean Entry Corridor"** identify karta hai aur live telemetry GCS ko stream karta hai.
   * Disaster sector ke upar pahunch kar apne andhar docked palm-sized micro drones ko deploy karta hai.

2. **Child UAV Swarm (Distributed Independent Surveillance - 4 Nodes):**
   * Deploy hone ke baad, 4 child drones aapas mein ad-hoc MANET mesh network ke through connected rehte hain.
   * Yeh decentralized **CBBA algorithm** run karte hain jisse aapas mein coordinates automatically distribute ho jate hain (*"Tum Sector-A me jao, main Sector-B survey karta hoon"*).
   * Har drone independent lawnmower search pattern execute karta hai, Edge AI (TensorRT) se survivors detect karta hai, aur multi-hop relay ke zariye data GCS tak pahunchata hai.

---

## 📁 Repository Structure
```text
Zerythron-VectorX/
│
├── README.md                      👉 Project documentation & architecture overview
├── package.xml                    👉 ROS 2 package metadata & dependencies
├── CMakeLists.txt                 👉 ROS 2 build configuration file
│
├── swarm_core/                    👉 Core intelligence & ROS 2 nodes
│   ├── __init__.py                👉 Python package initialization
│   └── swarm_planner.py           👉 CBBA task allocator & coordinate sharing node
│
├── mesh_comm/                     👉 MANET communication layer
│   ├── __init__.py                👉 Python package initialization
│   └── comms_manager.py           👉 Multi-hop relay manager & link quality estimator
│
└── px4_sitl_worlds/               👉 Simulation environment
    └── urban_disaster.world       👉 Disaster arena model for Gazebo SITL

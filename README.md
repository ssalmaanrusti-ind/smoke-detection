# 🔥 Smoke Detection System with Face Recognition

<p align="center">
  <b>Real-Time AI-Based Smoke Detection 🚭 | Face Recognition 👤 | Email Alerts 📧</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv">
  <img src="https://img.shields.io/badge/YOLOv5-Detection-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

---

## 📌 Project Overview

This project is an **AI-powered Smoke Detection System** that monitors live video feed using a webcam and detects smoking activity in real-time.

It integrates:

* 🔍 Deep Learning for smoke detection (YOLO ONNX model)
* 👤 Face Recognition to identify individuals
* 📧 Email alert system with captured evidence
* 🖥️ GUI-based interface using Tkinter

---

## 🎯 Key Features

✨ Real-time smoke detection
✨ Face recognition-based identification
✨ Automatic email alerts with image proof
✨ Admin & User login system
✨ Smoke detection logs with date & time
✨ GUI interface for easy interaction

---

## 🧠 System Workflow

```mermaid
graph TD
A[Start Camera] --> B[Detect Face]
B --> C[Detect Smoke]
C --> D{Smoke Found?}
D -->|Yes| E[Identify Person]
E --> F[Capture Image]
F --> G[Send Email Alert]
G --> H[Save Log]
D -->|No| B
```

---

## 🛠️ Tech Stack

| Technology  | Usage            |
| ----------- | ---------------- |
| Python      | Core Programming |
| OpenCV      | Video Processing |
| NumPy       | Data Handling    |
| Tkinter     | GUI Interface    |
| PIL         | Image Processing |
| ImageHash   | Face Matching    |
| YOLO (ONNX) | Smoke Detection  |
| SMTP        | Email Alerts     |

---
---

## 📥 Download Model

Due to GitHub file size limits, the model file is not included in this repository.

👉 Download the model from here:  
https://drive.google.com/file/d/1PzcYuw_z3TBnWw-EcAt_kng7eiAbgXoQ/view?usp=drive_link

### 📌 Instructions
1. Download the file `nm.onnx`
2. Place it inside the project folder:


## 📂 Project Structure

```bash
.
├── home.py
├── nm.onnx
├── train/
├── fine/
├── frame/
├── images/
├── data/haarcascades/
├── ar_master.py
└── README.md
```

---

## ▶️ Installation & Setup

### 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/ssalmaanrusti-ind/smoke-detection-system.git
cd smoke-detection-system
```

### 🔹 Step 2: Install Dependencies

```bash
pip install opencv-python numpy pillow imagehash
```

### 🔹 Step 3: Run the Project

```bash
python home.py
```

---

## 📧 Email Alert System

When smoke is detected:

* 📸 Captures image
* 👤 Identifies user
* 📅 Adds timestamp
* 📧 Sends alert to:

  * User
  * Admin (Head)

---

## 🔐 User Roles

### 👨‍💼 Admin (Head)

* Add Users
* View Users
* Monitor Smoke Logs

### 👤 User

* Login
* View personal detection history

---

## ⚠️ Requirements

* Webcam 📷
* Python 3.x
* Internet connection 🌐

---

## 🚀 Future Enhancements

* 🔥 Improve detection accuracy
* 🌐 Convert to web application
* 📱 Mobile app integration
* 📊 Live monitoring dashboard

---

## 👨‍💻 Author

    S.SALMAAN RUSTI

---

## ⭐ Show Your Support

If you like this project:

🌟 Star this repository
🍴 Fork it
🛠️ Contribute

---

## 📜 License

This project is for educational purposes only.

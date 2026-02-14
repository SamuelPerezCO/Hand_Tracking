# Hand Tracking with Python

A computer vision project to track hand movements in real time using Python

This project was created as a **personal review and practice** to reinforce previously learned concepts and improve logical thinking through hands-on development

---

## 📌 Features

- Real-time hand detection using a camera
- Hand landmarks visualization
- Finger state detection (up / down)
- Finger counting from 1 to 5
- Special gesture detection (middle finger only)
- Text rendering on screen based on gestures
- Works with webcam or mobile phone camera
- Optimized for Linux systems

---

## 🛠 Technologies Used

- Python 3
- OpenCV
- MediaPipe

---

## 📂 Project Structure

Hand_Tracking/
│
├─ src/
│ ├─ main.py
│ ├─ hand_tracking.py
│ └─ open_webcam.py
│
├─ venv/
├─ .gitignore
├─ requirements.txt
└─ README.md


---

## ⚙️ Installation

Clone the repository:

```bash
git clone <https://github.com/SamuelPerezCO/Hand_Tracking>
cd Hand_Tracking


python3 -m venv venv
source venv/bin/activate


pip install -r requirements.txt


python src/main.py
```
Press Q to close the application window

## 🧠 How It Works

The camera captures video frames in real time

MediaPipe detects the hand and extracts landmarks

Each finger is analyzed based on landmark positions

Fingers are counted by checking which ones are raised

Special gestures trigger specific messages on screen

The thumb is detected differently depending on whether the hand is left or right


## 🐧 Linux Notes

Tested on Linux environments

Uses OpenCV window rendering

Compatible with external cameras and mobile phone cameras

Warning messages from MediaPipe or Qt do not affect functionality

## 🎯 Purpose of the Project

The main purpose of this project is learning and practice, not production use

It helps reinforce:

Python fundamentals

Logical thinking

Computer vision basics

Hand landmark analysis

Project organization

Virtual environments

Git and GitHub workflow
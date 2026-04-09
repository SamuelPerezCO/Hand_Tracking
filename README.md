# Hand Gesture Detector

A real-time hand gesture recognition app using **OpenCV** and **MediaPipe**. It detects finger positions via webcam and identifies gestures like counting (1–5) and a special "middle finger" gesture.

---

## Features

- Real-time hand landmark detection via webcam
- Recognizes the following gestures:
  - **ONE** – Index finger up
  - **TWO** – Index + Middle fingers up
  - **THREE** – Index + Middle + Ring fingers up (or Middle + Ring + Pinky)
  - **FOUR** – All fingers up except thumb
  - **FIVE** – All fingers up including thumb
  - **FUCK YOU** – Middle finger only (+ optional system shutdown 😅)
- Displays fingertip labels and landmark circles on the video feed
- Mirror (flipped) view for a more natural experience

---

## Requirements

- Python 3.8+
- Webcam

### Dependencies

```bash
pip install opencv-python mediapipe
```

---

## Installation

```bash
git clone https://github.com/your-username/hand-gesture-detector.git
cd hand-gesture-detector
pip install opencv-python mediapipe
```

---

## Usage

```bash
python main.py
```

- A window named **"Image"** will open showing the webcam feed.
- Hold your hand in front of the camera to trigger gesture detection.
- Press **`q`** to quit.

---

## Project Structure

```
hand-gesture-detector/
│
└── main.py       # Main script
```

---

## How It Works

1. Captures frames from the webcam using OpenCV.
2. Flips the frame horizontally for a mirror view.
3. Passes the frame to MediaPipe Hands for landmark detection.
4. Evaluates the Y (and X for the thumb) coordinates of each fingertip relative to its base joint to determine whether each finger is up or down.
5. Matches the combination of raised fingers to a known gesture and overlays the label on screen.

---

## Configuration

You can tweak the following parameters inside `main.py`:

| Parameter | Default | Description |
|---|---|---|
| `max_num_hands` | `1` | Maximum number of hands to detect |
| `min_detection_confidence` | `0.7` | Minimum confidence for initial detection |
| `min_tracking_confidence` | `0.7` | Minimum confidence for tracking |
| Camera width | `1280` | Webcam capture width |
| Camera height | `720` | Webcam capture height |

---

## Notes

- The script contains a commented-out `os.system("shutdown now")` line triggered by the middle finger gesture. Uncomment at your own risk.
- Thumb detection is based on the X axis and may behave differently depending on which hand is used. Currently optimized for the **right hand**.

---

## License

MIT License
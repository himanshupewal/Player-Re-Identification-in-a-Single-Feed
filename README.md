# ⚽ Player Re-Identification in a Single Feed

This project implements a **player detection and re-identification system** using a YOLO object detection model on a single video feed.  
It detects players, assigns unique IDs based on their initial appearance, and tracks them across frames — maintaining the same IDs even when players temporarily leave and re-enter the frame.

---

## 📽️ Objective

Given a short video:
- Detect players in each frame.
- Assign each detected player a unique ID.
- If a player leaves the frame and returns later, recognize and reassign the same ID.
- Simulate real-time player tracking by generating an annotated output video with bounding boxes and IDs.

---

---

## 📖 How It Works

1️⃣ **Player Detection**
- Uses a YOLO model (via the Ultralytics library) to detect players in each video frame.
- Returns bounding boxes and class confidences for detected players.

2️⃣ **ID Assignment**
- In the first few frames, assigns a unique numeric ID to each detected player.

3️⃣ **Re-Identification Logic**
- Uses **IoU (Intersection over Union)** to compare each new detection's bounding box to previously tracked players' bounding boxes.
- If the IoU between a new detection and an existing player's last known position exceeds a defined similarity threshold (default 0.85), the same ID is assigned.
- If no match is found, a new ID is created for the player.

4️⃣ **Output Video Generation**
- Draws bounding boxes and player IDs on each video frame.
- Combines these frames into an annotated output video and saves it at `output/output_annotated.mp4`.

---

## 🚀 Installation & Setup

### 1️⃣ Install Python
Ensure Python 3.8 or later is installed on your system. You can download it from:
https://www.python.org/downloads/

### 2️⃣ Install Required Python Libraries

Install the necessary libraries listed in `requirements.txt` by running:

```bash
pip install -r requirements.txt

Contents of requirements.txt:
opencv-python
ultralytics
scikit-learn
numpy

 3️⃣ Prepare Files
Place your input video inside the videos/ directory.
Example: videos/15sec_input_720p.mp4

Place your YOLO model file inside the model/ directory.
Example: model/yolo_model.pt
(Note: Since this file is large — around 186 MB — it isn't stored on GitHub. Download it separately if needed.)


4️⃣ Run the Program
In your terminal or command prompt, navigate to your project directory and run:

python main.py


# ⚽ Player Re-Identification in a Single Feed

This project implements a **player detection and re-identification system** using a YOLO object detection model on a single video feed.  
It detects players, assigns unique IDs based on their initial appearance, and tracks them across frames — maintaining the same IDs even when players temporarily leave and re-enter the frame.

---

## 📽️ Objective

Given a short video:
- Detect players in each frame.
- Assign each player a unique ID.
- When a player leaves and reappears, recognize and reassign the same ID.
- Simulate real-time tracking with annotated output video.

---

## 📌 Project Structure


---

## 📖 How It Works  

1. **Player Detection**  
   - Uses a YOLO model to detect players in each video frame.
   - Returns bounding boxes for detected players.

2. **ID Assignment**  
   - In the initial frames, assigns a unique ID to each detected player.

3. **Re-Identification Logic**  
   - Compares each detected player's bounding box with previously tracked players using **IoU (Intersection over Union)** similarity.
   - If similarity exceeds a threshold (default 0.85), assigns the same ID.
   - If no match is found, assigns a new ID.

4. **Output Generation**  
   - Draws bounding boxes and player IDs on the frames.
   - Writes the annotated frames into an output video.

---

## 🚀 Installation & Setup  

### 1️⃣ Install Dependencies  

Make sure Python ≥ 3.8 is installed.  
Then install the required libraries:

```bash
pip install -r requirements.txt

requirements.txt
opencv-python
ultralytics
scikit-learn
numpy

▶️ Usage
Run the main program:
python main.py
What happens:

Reads videos/15sec_input_720p.mp4

Detects and tracks players, assigns IDs

Outputs annotated video to output/output_annotated.mp4

✨ Example Output
Input: A 15-second football video.

Output: Same video with colored bounding boxes and stable player IDs displayed above each player’s head — IDs maintained even after re-entries.

Notes
You can adjust the similarity threshold or model path inside detect_and_track.py as needed.

Make sure the video and model files exist at the expected locations before running.

No virtual environment setup is forced — you can install dependencies globally or inside any environment you prefer.
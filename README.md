# ⚽ Player Re-Identification in a Single Video Feed 🎥

This project performs player re-identification in a football match video using object detection and consistent ID tracking techniques. It uses a YOLO model for player detection and applies multi-object tracking to assign consistent IDs as players leave and re-enter the frame.

---
YOLO Architecture Overview
Developed by Ultralytics. This architecture builds upon previous versions with significant improvements in speed, accuracy, and flexibility, making it ideal for player detection in sports analytics.
```mermaid
graph TD
    A[Input Image] --> B[Backbone]
    B --> C[Neck]
    C --> D[Head]
    D --> E[Predictions]
```


## 📂 Project Structure
```
player-reidentification/
├── model/                   # YOLO model weights
│   └── yolov8s.pt           # Pretrained detection model
├── videos/                  # Input videos
│   └── match.mp4            # Sample input video
├── output/                  # Processed outputs
│   ├── annotated.mp4        # Annotated video
│   └── player_tracks.csv    # Tracking data
├── player_tracker.py        # Main tracking script
├── requirements.txt         # Dependency list
└── README.md                # Project documentation
```
---

## 📋 Features

- Detect players in a video using a YOLO model.
- Track players using consistent IDs as they move in and out of the frame.
- Re-identify players upon re-entry based on detection and tracking.
- Annotate the video feed with bounding boxes and IDs.

---

# 🛠️ Installation & Setup

### 📥 Clone the Repository

```bash
git clone https://github.com/yourusername/player-reidentification.git
cd player-reidentification
```
### 📦 Install Required Python Libraries
Install the necessary libraries listed in requirements.txt by running:
```bash
pip install -r requirements.txt
```
#### Contents of requirements.txt:
```torch
opencv-python    #for video reading, processing, and writing
numpy            # for array manipulations and numerical operations
ultralytics      # for YOLO detection
scikit-learn     #for cosine_similarity 
```
## 📁 Prepare Files
Before running the program, make sure the necessary files are correctly placed in the project directories:

### 🎥 Input Video

Place your input video file inside the videos/ directory.
``
videos/match.mp4
``

Place your YOLO model file inside the model/ directory.
``
model/yolo_model.pt
``

**⚠️ Note: The YOLO model file is large (~186 MB) and should be downloaded separately from the Ultralytics YOLO repo.**

## ▶️ Run the Program
Open your terminal or command prompt, navigate to your project’s main directory, and run:
```
python main.py
```
### 📊 Output
*The video will be displayed with bounding boxes and assigned IDs to each player.*

*Consistent IDs will be maintained even as players leave and re-enter the frame.*

#### 📌 Notes
Ensure Python 3.8 or later is installed on your system. Download it from: ``https://www.python.org/downloads/``

**Adjust main.py to modify detection thresholds or customize tracking behavior.**

import cv2
from ultralytics import YOLO
from src.utils import compute_similarity

def detect_and_track_players(video_path, model_path, output_path):
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError(f"Unable to open video: {video_path}")

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    next_player_id = 1
    tracked_players = {}

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        detections = results[0].boxes.xyxy.cpu().numpy()

        current_frame_ids = {}

        for det in detections:
            x1, y1, x2, y2 = det[:4]
            bbox = [x1, y1, x2, y2]

            matched_id = None
            max_sim = 0.0

            for pid, prev_bbox in tracked_players.items():
                sim = compute_similarity(bbox, prev_bbox)
                if sim > 0.85 and sim > max_sim:
                    matched_id = pid
                    max_sim = sim

            if matched_id is None:
                matched_id = next_player_id
                next_player_id += 1

            tracked_players[matched_id] = bbox
            current_frame_ids[matched_id] = bbox

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f'ID {matched_id}', (int(x1), int(y1)-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        out.write(frame)

    cap.release()
    out.release()
    print(f"Video saved to {output_path}")

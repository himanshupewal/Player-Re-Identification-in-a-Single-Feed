from src.detect_and_track import detect_and_track_players

def main():
    video_path = "videos/15sec_input_720p.mp4"
    model_path = "model/yolo_model.pt"
    output_path = "output/output_annotated.mp4"

    detect_and_track_players(video_path, model_path, output_path)

if __name__ == "__main__":
    main()

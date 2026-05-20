!pip install ultralytics
from ultralytics import YOLO
model = YOLO('yolo11n.pt')
model.predict(source="/content/2165-155327596_tiny.mp4",save=True)

# Object Detection using YOLO

from ultralytics import YOLO

# Load pre-trained YOLO model
model = YOLO("yolo11n.pt")

# Detect objects in image
results = model.predict(
    source="image.jpg",
    save=True,
    conf=0.25
)

# Display detected objects
for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        print(
            "Object:",
            model.names[class_id],
            "Confidence:",
            round(confidence * 100, 2),
            "%"
        )

print("Object Detection Completed!")

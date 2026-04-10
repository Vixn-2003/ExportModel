from ultralytics import YOLO

# Load model
model = YOLO("yolov10l.pt")

# Export ONNX với imgsz=640
model.export(format="onnx",opset=13, simplify=True)

print("✅ Export ONNX thành công (imgsz=640)")
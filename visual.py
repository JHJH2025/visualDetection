import cv2
from ultralytics import YOLO

#Testin Testing
print("test test")

# Load a pretrained YOLOv8 model
model = YOLO('yolov8n.pt')

# Open the image
img = cv2.imread('cats.jpg')

# Perform object detection
results = model(img)

# Draw bounding boxes and labels on the image
for result in results:
    boxes = result.boxes
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        class_id = box.cls[0]
        conf = box.conf[0]
        label = model.names[int(class_id)]
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(img, f'{label} {conf:.2f}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

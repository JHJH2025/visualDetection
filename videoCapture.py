import cv2
from ultralytics import YOLO

# Load a pretrained YOLOv8 model
model = YOLO('yolov8n.pt')

#start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, frame = cap.read()
    results = model(frame, stream=True)

    #for boxes
    for result in results:
        boxes= result.boxes
        # for box coordinates
        for box in boxes:
            #bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            class_id = box.cls[0]
            # confidence level 
            conf = box.conf[0]
            label = model.names[int(class_id)]
                                                                        #RBG color
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 255), 2)
            cv2.putText(frame, f'{label} {conf:.2f}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)


    cv2.imshow('Webcam',frame)
    # press q to quit
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
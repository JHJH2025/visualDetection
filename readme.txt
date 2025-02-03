**SET UP**
import cv2
from ultralytics import YOLO

**Need to dowload the following module**
(error: ModuleNotFound)
pip install ultralytics opencv-python
(pip uninstall ultralytics)
-------------------------------------------------------------------------------------------
**visual.py explanation:**

1. mport Libraries: Import cv2 for image manipulation and YOLO from the ultralytics library.

2. Load a Model: Load a pre-trained YOLOv8 model. You can replace 'yolov8n.pt' with other YOLOv8 models like 'yolov8s.pt' or 'yolov8m.pt' for better accuracy (but with slower inference).

3.Read an Image: Load the image you want to analyze using cv2.imread().

4. Perform Detection: Use the model() function to detect objects in the image. 

5. Draw Bounding Boxes: Loop through the detection results and draw bounding boxes and labels on the image.
Display: Use cv2.imshow() to display the image with detected objects.
------------------------------------------------------------------------------------------
**videoCapture.py explanation:**

1. Import OpenCV: Import the cv2 module.

2. Create VideoCapture Object: Create a VideoCapture object, passing the path to your video file or a camera index (e.g., 0 for the default camera).

3. Loop to Read Frames: Use a while loop to continuously read frames from the video.

4. Check ret: Check the value of ret to ensure that a frame was successfully read.

5. Display Frame: Use cv2.imshow() to display the frame in a window.

6. Exit Condition: Press the 'q' key to exit the loop and close the window.
7. Release VideoCapture: Release the VideoCapture object and close all windows.

import cv2
from ultralytics import YOLO

model=YOLO("yolov8n.pt")
image=cv2.imread("krishna.jpg")
results=model(image)
annotated_image= results[0].plot()
import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
image = cv2.imread("krishna.jpg")
results = model(image)
annotated_image = results[0].plot()

# Resize to fit screen
annotated_image = cv2.resize(annotated_image, (400, 400))  # you can change these numbers



cv2.imshow("Annotated Image", annotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

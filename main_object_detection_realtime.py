import cv2
from yolo_predictions import YOLO_pred

# cap = cv2.VideoCapture('2_predictions/video_house.mp4')
cap = cv2.VideoCapture(0)
yolo = YOLO_pred(path_2_onnx_model='2_predictions/Model/weights/best.onnx', path_2_data_yaml='1_datapreparation/data_images/data.yaml')

while(True):
  ret, frame = cap.read()
  
  if ret == False:
    print('Unable to read video')
    break

  result = yolo.prediction(image=frame)
  
  cv2.imshow("Object Detection", result)
  
  if cv2.waitKey(1) == 27: # press escape to quit:
    break

cap.release()
cv2.destroyAllWindows()
import cv2
from yolo_predictions import YOLO_pred

yolo = YOLO_pred(path_2_onnx_model='2_predictions/Model/weights/best.onnx', path_2_data_yaml='1_datapreparation/data_images/data.yaml')
image = cv2.imread('2_predictions/street_image.jpeg')
result = yolo.prediction(image=image)
cv2.imshow('Yolo Predicton', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
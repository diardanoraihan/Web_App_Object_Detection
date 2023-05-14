import cv2
import numpy as np
import os
import yaml
from yaml.loader import SafeLoader

class YOLO_pred:
  def __init__(self, path_2_onnx_model, path_2_data_yaml):
    
    # Load the YAML file
    with open(path_2_data_yaml, 'r') as file:
      data_yaml = yaml.load(file, Loader=SafeLoader)

    self.labels = data_yaml['names']
    self.nc = data_yaml['nc']

    # Load the YOLO Model
    self.yolo = cv2.dnn.readNetFromONNX(path_2_onnx_model)
    self.yolo.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    self.yolo.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU) # If you have GPU environment with you, you can select DNN_TARGET_CUDA

  def prediction(self, image):

    # Get the image properties
    row, col, d = image.shape

    # Create a squared empty frame
    max_rc = max(row, col)
    input_image = np.zeros(shape=(max_rc, max_rc, 3), dtype=np.uint8)

    # Overlay the empty frame with our input image
    input_image[:row, :col] = image

    # Get the prediction
    INPUT_WH_YOLO = 640
    blob = cv2.dnn.blobFromImage(
      image=input_image, 
      scalefactor = 1/255, 
      size = (INPUT_WH_YOLO, INPUT_WH_YOLO), # Remember that we train our YOLO model with 640 pixels image
      swapRB = True, # Swap BGR format from OpenCV to RGB format
      crop = False
      )

    self.yolo.setInput(blob)

    preds = self.yolo.forward() # detection or prediction from YOLO

    # Initialize some variables to prepare for the filtering process
    detections = preds[0]
    boxes = []
    confidences = []
    classes = []

    # Width and height of the input image --> (1920, 1920)
    image_w, image_h = input_image.shape[:2]
    x_factor = image_w / INPUT_WH_YOLO # 1920 / 640
    y_factor = image_h / INPUT_WH_YOLO # 1920 / 640

    # Filter detection based on confidence score (0.4) and probability score (0.25)
    for i in range(len(detections)):
      row = detections[i]
      confidence = row[4]
      if confidence > 0.4:
        class_score = row[5:].max() # Take the maximum probability from the 20 objects
        class_id = row[5:].argmax() # Get the index position at which mas probability occur
        if class_score > 0.25:
          cx, cy, w, h = row[:4]
          # construct the bounding box from four values: left, top, width, and height
          left = int((cx - 0.5 * w) * x_factor)
          top = int((cy - 0.5 * h) * y_factor)
          width = int(w * x_factor)
          height = int(h * y_factor)
          
          box = np.array([left, top, width, height])
          
          # append values into the list
          confidences.append(confidence)
          boxes.append(box)
          classes.append(class_id)
  
    # Clean
    boxes_np = np.array(boxes).tolist()
    confidences_np = np.array(confidences).tolist()

    # Non Maximum Suppression
    # Return the index position we need to consider 
    index = np.array(cv2.dnn.NMSBoxes(bboxes = boxes_np, scores = confidences_np, score_threshold = 0.2, nms_threshold = 0.45)).flatten()

    # Draw the Bounding Box
    for idx in index:
      # Extract the bounding box
      x, y, w, h = boxes_np[idx]
      bb_conf = int(confidences[idx]*100)
      class_id = classes[idx]
      class_name = self.labels[class_id]
      bb_color = self.generate_colors(class_id)
      
      text = '{}: {}%'.format(class_name, bb_conf)

      # Draw the bounding box
      cv2.rectangle(img=image, pt1=(x, y), pt2=(x + w, y + h), color=bb_color, thickness=2)

      # Draw a text box to put text
      cv2.rectangle(img=image, pt1=(x, y - 30), pt2=(x + w, y), color=bb_color, thickness=-1) # thickness -1 to fill all the rectangle

      # Put Text inside the text box
      cv2.putText(img=image, text=text, org=(x, y - 10), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=0.7, color=(0, 0, 0), thickness=1)
    
    return image
  
  def generate_colors(self, ID):
    np.random.seed(10)
    colors = np.random.randint(100, 255, size=(self.nc, 3)).tolist()
    return tuple(colors[ID])
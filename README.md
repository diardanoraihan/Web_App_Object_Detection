# Web App Object Detection
Perform custom object detection using YOLO algorithm and deploy it via web app in Python

## Packages Installation on Mac
- Create your python virtual environment
`pip3 install virtualenv`
`virtualenv yolo_env`

- Install all packages in the `requirements.txt` file
`pip3 install -r requirements.txt`

- [Optional] Install prerequisites of labelImg package in our system to help us labeling the image
`brew install libxml2`
`brew install qt5`
`brew link qt5 --force`

- [Optional] Install labelImg package in your newly-created python environment
`source <python_virenv>/bin/activate`
`pip3 install --upgrade pip`
`pip3 install pyqt5 --config-settings --confirm-license= --verbose`
`pip3 install labelImg —verbose`

## What is Object Detection?

### Classification
- For a simple classification task, the images generally have a single dominant object and the whole image is classified accordingly.
<img width="665" alt="image" src="https://user-images.githubusercontent.com/17371142/235333744-1d1e02df-6ea2-4f01-ba4f-fbe25eb77098.png">

### Localization
- It is the next step of classification technique. To find the position of object in the image, we require the object to be localized.
- This localization is performed using regression provides bounding box (x_min, y_min, x_max, y_max).
<img width="664" alt="image" src="https://user-images.githubusercontent.com/17371142/235333800-7cdd0613-1e81-4b16-aa1a-e4e0fce451f9.png">

### Object Detection
- Object detection in simple words finds objects in image and categorizes or classifies them.
<img width="1063" alt="image" src="https://user-images.githubusercontent.com/17371142/235333847-b61e05dc-fded-47cb-a5a2-ee0f6c980739.png">
- __Bounding Box Coordinates__: the bounding boxes of the objects detected in the coordinates.
- __Labels__ labels or class names of the bounding boxes predicted above
- __Confidence Scores__ confidence or probability scores of the classes detected
<img width="667" alt="image" src="https://user-images.githubusercontent.com/17371142/235333923-633f8b29-f46a-43b6-97af-e3ddd4751ebf.png">

### Detection
- Detection is the case of identifying or detecting objects in images. 
- It includes both the task mentioned before and can be better understood in case of images with **multiple objects** to be detected.
<img width="767" alt="image" src="https://user-images.githubusercontent.com/17371142/235333973-af691e06-1f4a-4061-9f75-1a7cb1507719.png">

## Evaluating Object Detection Model
<img width="720" alt="image" src="https://user-images.githubusercontent.com/17371142/235334198-d3ac120d-1558-483d-af52-dea633abf482.png">

There are two major evaluation techniques that will perform for object detection model:
- Intersection Over Union (IoU)
- mean Average Precision (mAP)

### Intesection Over Union
<img width="1221" alt="image" src="https://user-images.githubusercontent.com/17371142/235334300-15a9b345-0ed2-4e09-9b0b-58e0beccaa34.png">

- In general, IoU > 50% is consider as good prediction. (~ mAP 0.5)

### mean Average Precision (mAP)
- In order to understand mAP, let's familiarize again with a confusion matrix as the representation for object detection model.
<img width="858" alt="image" src="https://user-images.githubusercontent.com/17371142/235334789-f204ea7f-8205-4c49-b9f3-f2e6475ad493.png">

- __True Positive__:
  - IoU > 50% (~ mAP 0.5)
  - Both belong to the correct class

- __False Negative__:
  - IoU > 50% (~ mAP 0.5)
  - Incorrect class prediction
 
- __False Positive__:
  - IoU < 50%
  - Correct class prediction

- __True Negative__:
  - No detection when there is no object.

<img width="550" alt="image" src="https://user-images.githubusercontent.com/17371142/235334944-b0d71698-bf17-4705-bd5f-3306077a70f3.png">


To evaluate object detection models like R-CNN and YOLO, the mean average precision (mAP) is used. The mAP compares the ground-truth bounding box to the detected box and returns a score. The higher the score, the more accurate the model is in its detections. (Source: https://blog.paperspace.com/mean-average-precision/)





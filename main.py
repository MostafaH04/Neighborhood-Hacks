import numpy as np
import cv2
import os
import tensorflow as tf
from PIL import Image
import time
from cont import modelPredict as predict

model = tf.keras.models.load_model('saved model/myModel')

cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, frame = cap.read()
    key = cv2.waitKey(1)

    res = predict(frame, model)
    
   
    
    print(res)
    cv2.putText(frame, res, (20,20), cv2.FONT_HERSHEY_PLAIN, 2, (255,180,0),2)
    h = frame.shape[0]
    w = frame.shape[1]
    cv2.rectangle(frame, (int((w/2)-(w/6)), int((h/2) - (h/3.5))), (int(w/2+w/6), int(h/2 + h/3.5)), (0,50,255), 2)    
    cv2.imshow("Feed", frame)

    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()


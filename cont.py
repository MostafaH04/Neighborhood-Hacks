import tensorflow as tf
import numpy as np
import cv2
import os
from PIL import Image
import imutils
from tensorflow.keras.preprocessing import image


def modelPredict(frame, model):
    frame_predict = imutils.resize(frame, width= 150)
    frame_predict = frame_predict[0:150, 0:150]
    frame_predict = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imwrite("test1.jpg", frame_predict)
    frame_predict = image.load_img('test1.jpg', target_size=(150, 112))
    frame_arr = image.img_to_array(frame_predict)
    frame_arr = np.expand_dims(frame_arr, axis=0)
    os.remove('test1.jpg')

    frame_predict = np.vstack([frame_arr])

    out = model.predict(frame_predict, batch_size = 10)
    if int(out[0][0]) == 0:
        return "Mask"

    else:
        return "No Mask"
        



import cv2
import os
import time 
import numpy as np
import imutils

count = 0
saveCount = 0

path = 'model\\test\\masks'

global countFiles
countFiles = 0

while os.path.exists(path + str(countFiles)):
    countFiles += 1
os.makedirs(path + str(countFiles))

cap = cv2.VideoCapture(0)


while cap.isOpened():
    success, frame = cap.read()
    key = cv2.waitKey(1)
    frame = imutils.resize(frame, width= 150)
    frame = frame[0:150, 0:150]
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    if key == ord('k'):
        if count %1 == 0:
            currentTime = time.time()
            cv2.imwrite(f"{path}{countFiles}/{saveCount} {currentTime}.png", frame)
            saveCount += 1
        count += 1

    cv2.imshow("vid", frame)

    if key == ord('q'):
        break

cap.release()
cap.destroyAllWindows()
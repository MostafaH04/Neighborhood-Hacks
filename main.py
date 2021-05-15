import cv2
import tensorflow as tf
from cont import modelPredict as predict

model = tf.keras.models.load_model('saved model/myModel')

predicted = False
prediction = None
done = False

rect_color = (100,100,100)

def mouseEvent (event, x, y, flags, param):
    global prediction
    global predicted
    global rect_color
    global done

    if x > 0 and x < w and y > 7*h/8 and y < h:
        if event == cv2.EVENT_LBUTTONDOWN:
            rect_color = (60,60,60)

        if event == cv2.EVENT_LBUTTONUP:
            rect_color = (100,100,100)

            if prediction == None: 
                if done == False:
                    prediction = predict(frame, model)
                    done = True
                print(prediction)
                predicted = True

            else:
                print("Reset")
                prediction = None
                predicted = False
                done = False

cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, frame = cap.read()
    key = cv2.waitKey(1)
    h = frame.shape[0]
    w = frame.shape[1]

    frameUsed = frame

    if predicted == True:
        text = prediction
        if prediction == "Mask":
            text_color = (180, 255,0)
        else:
            text_color = (0,50,200)
        text2 = "Reset"
    else:
        text_color = (255, 180, 0)
        text = "Press to Verify"
        text2 = "Validate"
    cv2.putText(frameUsed, text, (40,50), cv2.FONT_HERSHEY_PLAIN, 2, text_color,2)
    
    cv2.rectangle(frameUsed, (0,int(7*h/8)), (int(w),int(h)), rect_color, -1)
    cv2.rectangle(frameUsed, (0,int(7*h/8)), (int(w),int(h)), (255,255,255), 2)
    cv2.putText(frameUsed, text2, (int(13*w/32),int(61*h/64)), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255),2)

    cv2.rectangle(frameUsed, (int((w/2)-(w/6)), int((h/2) - (h/3.5))), (int(w/2+w/6), int(h/2 + h/3.5)), (0,50,255), 2)    
    
    cv2.imshow("Feed", frameUsed)
    cv2.setMouseCallback("Feed", mouseEvent)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()


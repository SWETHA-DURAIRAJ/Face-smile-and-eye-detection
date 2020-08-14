import cv2
import numpy as np
cap=cv2.VideoCapture(0)



face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade=cv2.CascadeClassifier("haarcascade_smile.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
while True:
    sucess,img=cap.read()
    gary=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gary,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,h+y),(0,0,225),3)
        smilegary=gary[y:y+h,x:x+w]
        smile = img[y:y+h,x:x+w]

        eyes=eye_cascade.detectMultiScale(smilegary,1.1,22)
        smiles = smile_cascade.detectMultiScale(smilegary, 1.7, 22)
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(smile, (ex, ey),(ex + ew, ey + eh), (0, 255, 0), 2)
        for (ex,ey,ew,eh) in smiles:

            cv2.rectangle(smile, (ex, ey), (ex + ew, ey + eh), (225, 0, 0), 2)

    cv2.imshow("dectection",img)
    k = cv2.waitKey(30) & 0xff7
    if k == 27:
       break
cap.release()
cv2.destroyAllWindows()






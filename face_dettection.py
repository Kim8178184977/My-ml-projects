import cv2
algo="face.xml"
haar_cascade=cv2.CascadeClassifier(algo)
cam = cv2.VideoCapture(0)
while True:
    _,img=cam.read()
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.2,2)
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(87,255,155),1)
    cv2.imshow("face_dettection",img)
    key=cv2.waitKey(1)
    if key == 27:
        break
cam.release()
cam.destroyallwindows()
import cv2
print(cv2.__version__)

dispW= 960
dispH= 720
flip = 2


#camSet = f'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method={flip} ! video/x-raw, width={dispW}, height={dispH}, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam = cv2.VideoCapture(camSet)


cam= cv2.VideoCapture(1) 
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

face_cascade=cv2.CascadeClassifier("/home/pourya/Desktop/pyPro/Cascade/face.xml")
eye_cascade=cv2.CascadeClassifier("/home/pourya/Desktop/pyPro/Cascade/eye.xml")


while True:
    ret, frame= cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),3)
        roi_gray=gray[y:y+h, x:x+w]
        Roi_color=frame[y:y+h, x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)

        for (xEye,yEye,wEye,hEye) in eyes:
            cv2.rectangle(Roi_color, (xEye,yEye),(xEye+wEye, yEye+hEye), (255,0,0), 2)

    if ret:
        cv2.imshow('nanoCam', frame)
        cv2.moveWindow('nanoCam',0,0)
        
        
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

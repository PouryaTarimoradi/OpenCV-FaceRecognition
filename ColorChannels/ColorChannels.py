import cv2
import numpy as np
print(cv2.__version__)

dispW= 640
dispH= 480
flip = 2


#camSet = f'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method={flip} ! video/x-raw, width={dispW}, height={dispH}, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam = cv2.VideoCapture(camSet)


cam= cv2.VideoCapture(1) 
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

blank=np.zeros([480,640,1], np.uint8)
#blank[0:240, 0:320]=125

while True:
    ret, frame= cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #print(frame.shape)
    #print(frame.size)
    #b=cv2.split(frame)[0]
    #g=cv2.split(frame)[1]
    #r=cv2.split(frame)[2]
    print(frame[1,1,1])

    b,g,r = cv2.split(frame)
    blue=cv2.merge((b,blank,blank))
    green=cv2.merge((blank,g,blank))
    red=cv2.merge((blank,blank,r))

    merge=cv2.merge((b,g,r))
    


    if ret:

        cv2.imshow("blue", blue)
        cv2.moveWindow("blue",720, 0)

        cv2.imshow("green", green)
        cv2.moveWindow("green",0, 800)

        cv2.imshow("red", red)
        cv2.moveWindow("red",720, 800)

        cv2.imshow("merge", merge)
        cv2.moveWindow("merge", 1500,0) 

        cv2.imshow('nanoCam', frame)
        cv2.moveWindow('nanoCam',0,0)
        
        
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

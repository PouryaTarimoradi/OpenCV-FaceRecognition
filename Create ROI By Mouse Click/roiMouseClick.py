import cv2
print(cv2.__version__)

goFlag=0
dispW= 960
dispH= 720
flip = 2
def mouse_click(event, x, y, flags, params):
    global x1,y1,x2,y2
    global goFlag
    if event==cv2.EVENT_LBUTTONDOWN:
        x1=x
        y1=y
        goFlag=0
    if event==cv2.EVENT_LBUTTONUP:
        x2=x
        y2=y
        goFlag=1

        

cv2.namedWindow("nanoCam")
cv2.setMouseCallback("nanoCam", mouse_click, )


#camSet = f'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method={flip} ! video/x-raw, width={dispW}, height={dispH}, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam = cv2.VideoCapture(camSet)


cam= cv2.VideoCapture(1) 
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

while True:
    ret, frame= cam.read()

    if ret:
        cv2.imshow('nanoCam', frame)
        if goFlag==1:
            frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),3)
            roi=frame[y1:y2,x1:x2]
            cv2.imshow("copy ROI", roi)
            cv2.moveWindow("copy ROI", 1050, 0)
        cv2.moveWindow('nanoCam',0,0)
        
        
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()



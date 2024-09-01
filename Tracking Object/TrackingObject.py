import cv2
import numpy as np
print(cv2.__version__)

def nothing(x):
    pass

cv2.namedWindow("Trackbars")
cv2.moveWindow("Trackbars", 1500,0)

cv2.createTrackbar("hueLow", "Trackbars", 50,179,nothing)
cv2.createTrackbar("hueHigh", "Trackbars", 100,179,nothing)

cv2.createTrackbar("hue2Low", "Trackbars", 50,179,nothing)
cv2.createTrackbar("hue2High", "Trackbars", 100,179,nothing)

cv2.createTrackbar("satLow", "Trackbars", 100,255,nothing)
cv2.createTrackbar("satHigh", "Trackbars", 255,255,nothing)

cv2.createTrackbar("valLow", "Trackbars", 100,255,nothing)
cv2.createTrackbar("valHigh", "Trackbars", 255,255,nothing)



dispW= 640
dispH= 480
flip = 2


#camSet = f'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method={flip} ! video/x-raw, width={dispW}, height={dispH}, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam = cv2.VideoCapture(camSet)


cam= cv2.VideoCapture(1) 
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

while True:
    ret, frame= cam.read()
    #rame=cv2.imread("smarties.png")
    cv2.imshow("nanoCam",frame)
    cv2.moveWindow("nanoCam",0,0)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    HL=cv2.getTrackbarPos("hueLow", "Trackbars")
    HH=cv2.getTrackbarPos("hueHigh", "Trackbars")

    HL2=cv2.getTrackbarPos("hue2Low", "Trackbars")
    HH2=cv2.getTrackbarPos("hue2High", "Trackbars")

    SL=cv2.getTrackbarPos("satLow", "Trackbars")
    SH=cv2.getTrackbarPos("satHigh", "Trackbars")

    VL=cv2.getTrackbarPos("valLow", "Trackbars")
    VH=cv2.getTrackbarPos("valHigh", "Trackbars")

    Lower_bound=np.array([HL,SL,VL])
    Upper_bound=np.array([HH,SH,VH])

    Lower_bound2=np.array([HL2,SL,VL])
    Upper_bound2=np.array([HH2,SH,VH])

    FGMask=cv2.inRange(hsv,Lower_bound, Upper_bound)
    FGMask2=cv2.inRange(hsv,Lower_bound2, Upper_bound2)
    FGMaskComp=cv2.add(FGMask,FGMask2)
    cv2.imshow("FGMaskComp", FGMaskComp)
    cv2.moveWindow("FGMaskComp", 0, 500)


    FG=cv2.bitwise_and(frame,frame, mask=FGMaskComp)
    cv2.imshow("FG", FG)
    cv2.moveWindow("FG", 500, 500)

    BGMask= cv2.bitwise_not(FGMaskComp)
    cv2.imshow("BGMask", BGMask)
    cv2.moveWindow("BGMask", 1000, 500)

    BG=cv2.cvtColor(BGMask,cv2.COLOR_GRAY2BGR)
    cv2.imshow("BG", BG)
    cv2.moveWindow("BG", 1450, 500)

    Final=cv2.add(FG,BG)
    cv2.imshow("Final", Final)
    cv2.moveWindow("Final", 500, 0)
        
        
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

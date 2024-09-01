import cv2
print(cv2.__version__)

dispW= 640
dispH= 480
flip = 2


#camSet = f'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method={flip} ! video/x-raw, width={dispW}, height={dispH}, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam = cv2.VideoCapture(camSet)


cam= cv2.VideoCapture(1) 
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

AI=cv2.imread("download.jpg")
AI=cv2.resize(AI,(130,130))
cv2.imshow("AI", AI)
cv2.moveWindow("AI",750,0)

AIGray=cv2.cvtColor(AI,cv2.COLOR_BGR2GRAY)
cv2.imshow("AIGray", AIGray)
cv2.moveWindow("AIGray",950,0)


_,BGMask=cv2.threshold(AIGray, 245, 255, cv2.THRESH_BINARY)
cv2.imshow("BGMask", BGMask)
cv2.moveWindow("BGMask",1150,0)


FGMask= cv2.bitwise_not(BGMask)
cv2.imshow("FGMask", FGMask)
cv2.moveWindow("FGMask",1350,0)

FG=cv2.bitwise_and(AI, AI, mask=FGMask)
cv2.imshow("FG", FG)
cv2.moveWindow("FG",1550,0)




BW=130
BH=130
Xpos=10
Ypos=10
dx=5
dy=5





while True:
    ret, frame= cam.read()
    ROI=frame[Ypos:Ypos+BH, Xpos:Xpos+BW]
    ROIBG=cv2.bitwise_and(ROI,ROI,mask=BGMask)
    cv2.imshow("ROIBG", ROIBG)
    cv2.moveWindow("ROIBG", 1750, 0)

    ROInew=cv2.add(FG,ROIBG)
    cv2.imshow("ROInew", ROInew)
    cv2.moveWindow("ROInew",1200,300)

    frame[Ypos:Ypos+BH, Xpos:Xpos+BW]=ROInew

    Xpos=Xpos+dx
    Ypos=Ypos+dy

    if Xpos<=0 or Xpos+BW>=dispW:
        dx=dx*(-1)
    
    if Ypos<=0 or Ypos+BH>=dispH:
        dy=dy*(-1)


    if ret:
        cv2.imshow('nanoCam', frame)
        cv2.moveWindow('nanoCam',0,0)
        
        
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

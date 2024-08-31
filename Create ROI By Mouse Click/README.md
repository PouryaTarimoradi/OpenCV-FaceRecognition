# OpenCV Region of Interest (ROI) Selection

This project demonstrates how to create an interactive Region of Interest (ROI) selection tool using OpenCV and Python. The script allows users to select a rectangular area on a live video feed using mouse clicks, and then displays the selected region in a separate window.

## Features

- Real-time video capture from a camera
- Interactive ROI selection using mouse clicks
- Display of the selected ROI in a separate window
- Support for both NVIDIA Jetson camera and Logitech webcam

## Prerequisites

- Python 3.x
- OpenCV library

## Installation

1. Ensure you have Python installed on your system.
2. Install OpenCV:
   ```
   pip install opencv-python
   ```
3. If you're using an NVIDIA Jetson, make sure you have the necessary camera drivers installed.

## Usage

1. Run the script:
   ```
   roiMouseClick.py
   ```
2. A window named "nanoCam" will open showing the live camera feed.
3. Click and drag on the video feed to select a region of interest.
4. The selected region will be displayed in a separate window named "copy ROI".
5. Press 'q' to exit the program.

## Code Explanation

```python
import cv2
print(cv2.__version__)

goFlag = 0
dispW = 960
dispH = 720
flip = 2

def mouse_click(event, x, y, flags, params):
    global x1, y1, x2, y2
    global goFlag
    if event == cv2.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y
        goFlag = 0
    if event == cv2.EVENT_LBUTTONUP:
        x2 = x
        y2 = y
        goFlag = 1

cv2.namedWindow("nanoCam")
cv2.setMouseCallback("nanoCam", mouse_click)

# Camera setup (uncomment the appropriate lines)
# For NVIDIA Jetson camera:
# camSet = f'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method={flip} ! video/x-raw, width={dispW}, height={dispH}, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam = cv2.VideoCapture(camSet)

# For Logitech webcam:
cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

while True:
    ret, frame = cam.read()
    if ret:
        cv2.imshow('nanoCam', frame)
        if goFlag == 1:
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
            roi = frame[y1:y2, x1:x2]
            cv2.imshow("copy ROI", roi)
            cv2.moveWindow("copy ROI", 1050, 0)
        cv2.moveWindow('nanoCam', 0, 0)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
```

### Key Components

1. **Mouse Callback Function**: `mouse_click()` handles mouse events to capture the start and end points of the ROI selection.

2. **Camera Setup**: The script supports both NVIDIA Jetson camera and Logitech webcam. Uncomment the appropriate lines for your setup.

3. **Main Loop**: Continuously captures frames from the camera, displays them, and handles the ROI selection and display.

4. **ROI Display**: When a region is selected (goFlag == 1), it draws a rectangle on the main frame and displays the selected region in a separate window.

## Customization

- Adjust `dispW` and `dispH` to change the display resolution.
- Modify the `flip` variable to change the camera orientation if needed.
- Change the rectangle color by modifying the BGR values in `cv2.rectangle()`.

## Troubleshooting

- If the camera doesn't open, ensure you're using the correct camera index or gstreamer pipeline.
- For NVIDIA Jetson users, make sure to uncomment the appropriate camSet lines and comment out the Logitech camera setup.

## Contributing

Feel free to fork this project, submit pull requests, or send suggestions to improve the code. All contributions are welcome!

## License

This project is open source and available under the MIT License.

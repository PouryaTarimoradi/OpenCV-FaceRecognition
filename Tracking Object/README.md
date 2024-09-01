# OpenCV Object Tracking by HSV Project

This project demonstrates real-time object tracking using HSV (Hue, Saturation, Value) color space in OpenCV. It allows users to dynamically adjust HSV thresholds to isolate and track objects of specific colors in a video feed.

## HSV-based Object Tracking

The core of this project revolves around HSV color space manipulation and thresholding:

```python
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
Lower_bound = np.array([HL, SL, VL])
Upper_bound = np.array([HH, SH, VH])
FGMask = cv2.inRange(hsv, Lower_bound, Upper_bound)
```

### Function Explanation

The object tracking in this project is based on these key OpenCV functions:

* `cv2.cvtColor()`: Converts the color space of an image (BGR to HSV in this case).
* `cv2.inRange()`: Creates a binary mask based on color thresholds.
* `cv2.bitwise_and()`: Applies a mask to an image.
* `cv2.add()`: Combines two images or masks.

These functions allow us to isolate objects of specific colors and visualize them separately from the background.

### Parameters

* `frame`: The input image captured from the camera
* `HL`, `HH`, `SL`, `SH`, `VL`, `VH`: Lower and upper bounds for Hue, Saturation, and Value
* `FGMask`: Foreground mask created by color thresholding
* `BGMask`: Background mask (inverse of the foreground mask)

### How it Works

1. The input frame is converted from BGR to HSV color space.
2. User-adjustable thresholds define the color range of interest.
3. A binary mask is created using these thresholds.
4. The mask is applied to the original frame to isolate the object of interest.
5. Various visualizations are created to show the tracking process.

## Project Overview

This project creates an interactive object tracking application:

1. The camera feed is captured in real-time.
2. Users can adjust HSV thresholds using trackbars.
3. Objects within the specified color range are isolated.
4. Multiple windows display different stages of the tracking process.
5. The process continues until the user terminates the program.

## Key Components

* Single camera setup (choice between NVIDIA Jetson camera and Logitech camera)
* OpenCV for image processing and display
* Real-time video manipulation
* HSV color space thresholding
* Interactive trackbars for threshold adjustment

## Usage

1. Ensure all dependencies are installed and the chosen camera is connected.
2. Uncomment the appropriate camera setup lines in the code:
   * For NVIDIA Jetson (pyCamera):
   ```python
   camSet = f'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method={flip} ! video/x-raw, width={dispW}, height={dispH}, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
   cam = cv2.VideoCapture(camSet)
   ```
   * For Logitech camera:
   ```python
   cam = cv2.VideoCapture(1)
   cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
   cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)
   ```
3. Run the script:
   ```
   python TrackingObjectByHSV.py
   ```
4. Multiple windows will open showing the camera feed and various stages of processing.
5. Use the trackbars to adjust HSV thresholds for object tracking.
6. Press 'q' to exit the program.

## Customization

You can modify these variables to change the behavior:
* `dispW` and `dispH`: Display width and height
* `flip`: Flip method for NVIDIA Jetson camera
* Initial values for trackbars in `cv2.createTrackbar()` calls
* Window positions using `cv2.moveWindow()`

## Applications of HSV-based Object Tracking

The techniques demonstrated in this project have various applications:

1. Robotics: Enabling robots to identify and track specific objects.
2. Industrial Automation: Sorting items based on color in manufacturing processes.
3. Augmented Reality: Tracking colored markers for AR applications.
4. Sports Analysis: Tracking balls or players with specific uniform colors.
5. Traffic Monitoring: Identifying vehicles of certain colors in traffic footage.

## Future Improvements

* Implement multi-object tracking
* Add shape detection to improve tracking accuracy
* Integrate with machine learning for more robust object recognition
* Implement object tracking across multiple cameras
* Add data logging and analysis features for tracked objects

## Contributing

Feel free to fork this project, submit pull requests, or send suggestions to improve the code. All contributions are welcome!

## License

This project is open source and available under the MIT License.

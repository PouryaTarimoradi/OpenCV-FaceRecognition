# OpenCV Face and Eye Detection Project

This project demonstrates real-time face and eye detection using Haar Cascade classifiers in OpenCV. It captures video from a camera and applies face and eye detection algorithms to each frame.

## Haar Cascade-based Face and Eye Detection

The core of this project revolves around using Haar Cascade classifiers for face and eye detection:

```python
face_cascade = cv2.CascadeClassifier("/home/pourya/Desktop/pyPro/Cascade/face.xml")
eye_cascade = cv2.CascadeClassifier("/home/pourya/Desktop/pyPro/Cascade/eye.xml")

# ...

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 3)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (xEye,yEye,wEye,hEye) in eyes:
        cv2.rectangle(roi_color, (xEye,yEye), (xEye+wEye, yEye+hEye), (255,0,0), 2)
```

### Function Explanation

The face and eye detection in this project is based on these key OpenCV functions:

* `cv2.CascadeClassifier()`: Loads the Haar Cascade XML files for face and eye detection.
* `detectMultiScale()`: Detects objects (faces or eyes) of different sizes in the input image.
* `cv2.rectangle()`: Draws rectangles around detected faces and eyes.

### Parameters

* `gray`: Grayscale version of the input frame
* `1.3`: Scale factor that specifies how much the image size is reduced at each image scale
* `5`: Minimum number of neighbors each candidate rectangle should have to retain it

### How it Works

1. The input frame is converted to grayscale.
2. The face cascade classifier detects faces in the grayscale image.
3. For each detected face:
   - A rectangle is drawn around it on the original frame.
   - A region of interest (ROI) is defined within the face area.
   - The eye cascade classifier detects eyes within this ROI.
   - Rectangles are drawn around detected eyes.

## Project Overview

This project creates a real-time face and eye detection application:

1. The camera feed is captured in real-time.
2. Each frame is processed for face detection.
3. Within each detected face, eye detection is performed.
4. Rectangles are drawn to highlight detected faces and eyes.
5. The process continues until the user terminates the program.

## Key Components

* Single camera setup (choice between NVIDIA Jetson camera and Logitech camera)
* OpenCV for image processing and display
* Haar Cascade classifiers for face and eye detection
* Real-time video processing

## Usage

1. Ensure OpenCV is installed and the camera is connected.
2. Place the Haar Cascade XML files (`face.xml` and `eye.xml`) in the specified directory.
3. Uncomment the appropriate camera setup lines in the code:
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
4. Run the script:
   ```
   python FaceAndEyeDetectionByHaarCascades.py
   ```
5. A window will open showing the camera feed with detected faces and eyes highlighted.
6. Press 'q' to exit the program.

## Customization

You can modify these variables to change the behavior:
* `dispW` and `dispH`: Display width and height
* `flip`: Flip method for NVIDIA Jetson camera
* Paths to the Haar Cascade XML files
* Detection parameters in `detectMultiScale()` calls

## Applications of Haar Cascade-based Detection

The techniques demonstrated in this project have various applications:

1. Security Systems: Identifying and tracking individuals in surveillance footage.
2. Human-Computer Interaction: Enabling eye-tracking or face-based control systems.
3. Photography: Automatic face detection for focus and exposure optimization.
4. Emotion Recognition: As a first step in detecting facial expressions.
5. Attendance Systems: Automating attendance tracking in schools or workplaces.

## Future Improvements

* Implement more robust face detection algorithms (e.g., deep learning-based methods)
* Add face recognition capabilities to identify specific individuals
* Optimize for better performance on edge devices
* Implement tracking to reduce frame-to-frame jitter in detections
* Add features like age and gender estimation based on detected faces

## Contributing

Feel free to fork this project, submit pull requests, or send suggestions to improve the code. All contributions are welcome!

## License

This project is open source and available under the MIT License.

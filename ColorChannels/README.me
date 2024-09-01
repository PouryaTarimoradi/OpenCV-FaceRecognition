# OpenCV Color Channels Project

This project demonstrates color channel manipulation using OpenCV and a single camera feed (either Logitech or Py camera). The core of this project is the separation and visualization of color channels, a fundamental concept in image processing and computer vision.

## Color Channel Separation

The heart of this project is the color channel separation and manipulation:

```python
b, g, r = cv2.split(frame)
blue = cv2.merge((b, blank, blank))
green = cv2.merge((blank, g, blank))
red = cv2.merge((blank, blank, r))
merge = cv2.merge((b, g, r))
```

### Function Explanation

The color channel manipulation in this project is based on these key OpenCV functions:

* `cv2.split()`: Separates the BGR image into its individual Blue, Green, and Red channels.
* `cv2.merge()`: Combines given channels into a single multi-channel array.

These functions allow us to isolate and visualize each color component of an image separately.

### Parameters

* `frame`: The input image captured from the camera
* `blank`: A blank (black) image used to create single-channel visualizations

### How it Works

1. The input frame is split into its Blue, Green, and Red components.
2. For each color channel, a new image is created by merging the channel with two blank images.
3. This results in three images, each showing only one color component.
4. The original channels are merged back to create a full-color image.

## Project Overview

This project uses color channel separation to create a real-time color component visualization:

1. The camera feed is captured in real-time.
2. Each frame is split into its color components.
3. Separate windows display the Blue, Green, and Red channels, as well as the original and merged images.
4. The process continues until the user terminates the program.

## Key Components

* Single camera setup (choice between NVIDIA Jetson camera and Logitech camera)
* OpenCV for image processing and display
* Real-time video manipulation
* Color channel separation and visualization

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
   python ColorChannels.py
   ```
4. Multiple windows will open showing the original feed and individual color channels.
5. Press 'q' to exit the program.

## Customization

You can modify these variables to change the behavior:
* `dispW` and `dispH`: Display width and height
* `flip`: Flip method for NVIDIA Jetson camera
* Window positions using `cv2.moveWindow()`

## Applications of Color Channel Manipulation

The color channel manipulation demonstrated in this project has wide-ranging applications:

1. Image Enhancement: Adjusting individual color channels for better image quality.
2. Color Correction: Modifying color balance in photos and videos.
3. Feature Extraction: Isolating specific colors for object detection or tracking.
4. Artistic Effects: Creating visual effects by manipulating color channels.
5. Medical Imaging: Enhancing specific features in medical scans.

## Future Improvements

* Implement more complex color space transformations (e.g., HSV, LAB)
* Add user controls for real-time color channel adjustments
* Integrate with other computer vision techniques for advanced image analysis
* Add option to switch between cameras dynamically
* Implement color-based object tracking

## Contributing

Feel free to fork this project, submit pull requests, or send suggestions to improve the code. All contributions are welcome!

## License

This project is open source and available under the MIT License.

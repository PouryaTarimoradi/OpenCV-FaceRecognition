# OpenCV Thresholding and Masking Project

This project demonstrates advanced image processing techniques using OpenCV, including thresholding, masking, and real-time video manipulation. It uses a single camera feed (either Logitech or Py camera) to create an interactive application that overlays a moving image on a live video feed.

## Thresholding and Masking

The core of this project revolves around thresholding and masking techniques:

```python
_, BGMask = cv2.threshold(AIGray, 245, 255, cv2.THRESH_BINARY)
FGMask = cv2.bitwise_not(BGMask)
FG = cv2.bitwise_and(AI, AI, mask=FGMask)
ROIBG = cv2.bitwise_and(ROI, ROI, mask=BGMask)
ROInew = cv2.add(FG, ROIBG)
```

### Function Explanation

The thresholding and masking in this project are based on these key OpenCV functions:

* `cv2.threshold()`: Creates a binary mask based on pixel intensity.
* `cv2.bitwise_not()`: Inverts a binary mask.
* `cv2.bitwise_and()`: Applies a mask to an image.
* `cv2.add()`: Combines two images.

These functions allow us to isolate specific parts of an image and combine them with others.

### Parameters

* `AIGray`: Grayscale version of the overlay image
* `BGMask`: Binary mask for the background
* `FGMask`: Inverted mask for the foreground
* `AI`: The original overlay image
* `ROI`: Region of Interest in the video frame

### How it Works

1. A binary mask is created from the grayscale overlay image.
2. The mask is inverted to create a foreground mask.
3. The masks are applied to isolate the foreground and background.
4. The isolated foreground is combined with the masked region of interest in the video frame.
5. The result is a seamless overlay of the image on the video feed.

## Project Overview

This project uses thresholding and masking to create a dynamic overlay on a video feed:

1. The camera feed is captured in real-time.
2. An overlay image is processed to create masks.
3. A region of interest in the video frame is defined and masked.
4. The overlay image is combined with the masked region.
5. The combined image moves across the video feed in a bouncing pattern.
6. The process continues until the user terminates the program.

## Key Components

* Single camera setup (choice between NVIDIA Jetson camera and Logitech camera)
* OpenCV for image processing and display
* Real-time video manipulation
* Image thresholding and masking
* Dynamic image overlay with animation

## Usage

1. Ensure all dependencies are installed and the chosen camera is connected.
2. Place the 'download.jpg' file in the same directory as the script.
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
   python ThresholdingAndMasking.py
   ```
5. Multiple windows will open showing different stages of image processing.
6. Press 'q' to exit the program.

## Customization

You can modify these variables to change the behavior:
* `dispW` and `dispH`: Display width and height
* `flip`: Flip method for NVIDIA Jetson camera
* `BW` and `BH`: Width and height of the bouncing image
* `dx` and `dy`: Speed and direction of the bouncing image
* Window positions using `cv2.moveWindow()`

## Applications of Thresholding and Masking

The techniques demonstrated in this project have various applications:

1. Object Tracking: Isolating objects of interest in a video stream.
2. Green Screen Effects: Creating custom backgrounds for video production.
3. Image Segmentation: Separating foreground and background in images.
4. Watermarking: Adding logos or text overlays to videos.
5. Augmented Reality: Integrating virtual objects into real-world video.

## Future Improvements

* Implement more complex thresholding techniques (e.g., adaptive thresholding)
* Add user controls for real-time adjustment of thresholding parameters
* Integrate with facial recognition for smart overlay positioning
* Add option to use custom overlay images
* Implement more advanced animation patterns for the overlay

## Contributing

Feel free to fork this project, submit pull requests, or send suggestions to improve the code. All contributions are welcome!

## License

This project is open source and available under the MIT License.

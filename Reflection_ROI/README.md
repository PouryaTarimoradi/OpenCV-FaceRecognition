# Reflection with Masking and Grayscale Background

## Introduction

This project is a continuation of our previous OpenCV learning journey, building directly upon the reflection code we developed earlier. While retaining the core reflection mechanics, this version introduces advanced image processing techniques using OpenCV, specifically focusing on masking and grayscale effects.

## Background

In our previous project, we implemented a simple reflection algorithm that allowed a rectangle to bounce around the screen, demonstrating basic physics principles. This current project takes that foundation and enhances it with more sophisticated visual effects.

## New Features

- Grayscale background with a colored moving rectangle
- Mask-based color preservation
- Real-time video processing with dynamic visual effects

## Key Additions

### Grayscale Conversion
The entire frame is converted to grayscale, creating a stark contrast for the colored rectangle:

```python
frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frame_gray = cv2.cvtColor(frame_gray, cv2.COLOR_GRAY2BGR)
```

### Masking for Color Preservation
A binary mask is created to isolate the rectangle area:

```python
mask = np.zeros(frame.shape[:2], dtype=np.uint8)
cv2.rectangle(mask, (int(X_Coordinate), int(Y_Coordinate)),
              (int(X_Coordinate + rectangle_width), int(Y_Coordinate + rectangle_height)), 255, -1)
```

### Applying the Mask
The original colors of the rectangle are preserved by copying the masked area from the original frame to the grayscale frame:

```python
frame_gray[mask == 255] = frame[mask == 255]
```

## How It Works

1. The camera feed is converted to grayscale.
2. A mask is created in the shape of the rectangle.
3. The colored rectangle is superimposed on the grayscale background using the mask.
4. The rectangle moves and reflects off the edges as in the previous version.
5. The process repeats for each frame, creating a dynamic visual effect.

## Improvements from Previous Version

- Enhanced visual contrast between the moving object and the background
- Demonstration of advanced OpenCV techniques like masking and color space conversion
- More complex image processing pipeline, showcasing real-time video manipulation skills

## Usage

The usage remains similar to the previous version. Ensure you have the correct camera setup uncommented in the code:

For NVIDIA Jetson (pyCamera):
```python
camSet = f'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method={flip} ! video/x-raw, width={dispW}, height={dispH}, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)
```

For Logitech camera:
```python
cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)
```

Run the script:
```
python reflection_with_masking.py
```

Press 'q' to exit the program.

## Key Components

- Single camera setup (choice between NVIDIA Jetson camera and Logitech camera)
- OpenCV for image processing and display
- Real-time video manipulation
- Physics-based reflection calculation (retained from the previous version)
- Numpy for efficient array operations and masking

## Customization

You can modify these variables to change the behavior:
- `rectangle_width` and `rectangle_height`: Size of the rectangle
- `angle`: Initial angle of movement
- `speed`: Speed of the rectangle
- The additional rotation after reflection (currently set to 70 degrees)

## Applications

This project demonstrates several concepts applicable in various fields:

1. Computer Graphics: Simulating reflections and color manipulations
2. Image Processing: Using masks for selective color preservation
3. Computer Vision: Real-time video processing and object tracking
4. Game Development: Creating dynamic object movements and interactions
5. Educational Tools: Visualizing physics concepts like reflection and vector mathematics

## Future Ideas

- Implement multiple moving objects with different colors
- Add user controls to adjust the grayscale intensity or apply other color filters
- Incorporate shape detection to make the mask adapt to detected objects in the frame
- Experiment with different color spaces for more complex visual effects
- Integrate object detection to make the rectangle interact with real objects in the camera feed

## Conclusion

This project demonstrates the power of combining basic computer vision techniques with more advanced image processing. It builds upon our previous work with reflections and introduces new concepts in masking and color manipulation. This serves as a stepping stone for more complex OpenCV projects and provides a visual representation of masking and color space manipulation concepts.

## Contributing

Feel free to fork this project, submit pull requests, or send suggestions to improve the code. All contributions are welcome!

## License

This project is open source and available under the [MIT License](../LICENSE).

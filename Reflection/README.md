# OpenCV Reflection Project

This project demonstrates a bouncing rectangle with reflection using OpenCV and dual camera feeds from Logitech and Py cameras. The core of this project is the implementation of the reflection formula, a fundamental concept in physics and computer graphics.

## Reflection Function

The heart of this project is the `reflect` function:

```python
def reflect(dx, dy, normal_x, normal_y):
    dot_product = dx * normal_x + dy * normal_y
    reflection_x = dx - 2 * dot_product * normal_x
    reflection_y = dy - 2 * dot_product * normal_y
    return reflection_x, reflection_y
```

### Formula Explanation

The reflection formula used in this function is based on the vector reflection equation:

R = V - 2(V · N)N

Where:
- R is the reflection vector
- V is the incident vector (the original direction)
- N is the normal vector of the surface
- · represents the dot product

This formula calculates how a vector (in our case, the movement direction of the rectangle) reflects off a surface.

### Parameters

- `dx`, `dy`: Components of the incident vector (current movement direction)
- `normal_x`, `normal_y`: Components of the normal vector of the reflecting surface

### How it Works

1. Calculate the dot product of the incident vector and the normal vector.
2. Multiply this by 2 and by the normal vector.
3. Subtract this result from the original incident vector to get the reflection vector.

## Project Overview

This project uses the reflection function to create a bouncing rectangle effect on two camera feeds:

1. The rectangle moves across the screen with an initial angle and speed.
2. When it hits an edge, the `reflect` function is called to calculate the new direction.
3. An additional rotation is applied after reflection for more dynamic movement.
4. The rectangle is drawn on both camera feeds (pyCamera and Logitech Camera).

## Key Components

- Dual camera setup (NVIDIA Jetson camera and Logitech camera)
- OpenCV for image processing and display
- Real-time video manipulation
- Physics-based reflection calculation

## Usage

1. Ensure all dependencies are installed and cameras are connected.
2. Run the script:
   ```
   python reflection.py
   ```
3. Two windows will open showing the camera feeds with the bouncing rectangle.
4. Press 'q' to exit the program.

## Customization

You can modify these variables to change the behavior:
- `rectangle_width` and `rectangle_height`: Size of the rectangle
- `angle`: Initial angle of movement
- `speed`: Speed of the rectangle
- The additional rotation after reflection (currently set to 70 degrees)

## Applications of Reflection

The reflection concept demonstrated in this project has wide-ranging applications:

1. Computer Graphics: Used in rendering realistic light reflections in 3D scenes.
2. Game Physics: Crucial for simulating ball movements, particle effects, etc.
3. Optics: Modeling behavior of light in lenses and mirrors.
4. Sound Engineering: Simulating sound reflections in acoustic modeling.
5. Robotics: Planning movements and reactions to obstacles.

## Future Improvements

- Implement more complex reflection scenarios 
- Add user controls for rectangle properties and reflection parameters
- Integrate with other computer vision techniques for object detection and tracking

## Contributing

Feel free to fork this project, submit pull requests, or send suggestions to improve the code. All contributions are welcome!

## License

This project is open source and available under the [MIT License](../LICENSE).

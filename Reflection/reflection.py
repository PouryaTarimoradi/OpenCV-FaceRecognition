import cv2
import time
import math

# Print OpenCV version for debugging
print(cv2.__version__)

# Initial position of the rectangle
X_Coordinate = 0
Y_Coordinate = 0

# Rectangle dimensions
rectangle_width = 50
rectangle_height = 50

# Display dimensions for both cameras
dispW_py = 640
dispH_py = 480
dispW_log = 640
dispH_log = 480

# Flip method for NVIDIA camera
flip = 2

# Initialize movement vector
angle = math.radians(80)  # Start at 80 degrees
speed = 5
dx = speed * math.cos(angle)
dy = speed * math.sin(angle)

# Camera setup for NVIDIA Jetson
camSet = f'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method={flip} ! video/x-raw, width={dispW_py}, height={dispH_py}, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam = cv2.VideoCapture(camSet)

# Setup for Logitech camera
cam_log = cv2.VideoCapture(1)
cam_log.set(cv2.CAP_PROP_FRAME_WIDTH, dispW_log)
cam_log.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH_log)

def reflect(dx, dy, normal_x, normal_y):
    """
    Calculate the reflection vector.
    
    Args:
    dx, dy: Components of the incident vector
    normal_x, normal_y: Components of the normal vector
    
    Returns:
    reflection_x, reflection_y: Components of the reflection vector
    """
    dot_product = dx * normal_x + dy * normal_y
    reflection_x = dx - 2 * dot_product * normal_x
    reflection_y = dy - 2 * dot_product * normal_y
    return reflection_x, reflection_y

# Main loop
while True:
    # Capture frames from both cameras
    ret_py, frame_py = cam.read()
    ret_log, frame_log = cam_log.read()
    
    if ret_py and ret_log:
        # Update position
        X_Coordinate += dx
        Y_Coordinate += dy
        
        # Check for collisions with horizontal edges
        if X_Coordinate <= 0 or X_Coordinate >= dispW_py - rectangle_width:
            normal_x = -1 if X_Coordinate <= 0 else 1
            normal_y = 0
            dx, dy = reflect(dx, dy, normal_x, normal_y)
            
            # Add additional rotation for more dynamic movement
            angle = math.atan2(dy, dx)
            angle += math.radians(70)  # Add 70 degrees
            dx = speed * math.cos(angle)
            dy = speed * math.sin(angle)
            
            # Ensure rectangle stays within bounds
            X_Coordinate = max(0, min(X_Coordinate, dispW_py - rectangle_width))
        
        # Check for collisions with vertical edges
        if Y_Coordinate <= 0 or Y_Coordinate >= dispH_py - rectangle_height:
            normal_x = 0
            normal_y = -1 if Y_Coordinate <= 0 else 1
            dx, dy = reflect(dx, dy, normal_x, normal_y)
            
            # Add additional rotation for more dynamic movement
            angle = math.atan2(dy, dx)
            angle += math.radians(70)  # Add 70 degrees
            dx = speed * math.cos(angle)
            dy = speed * math.sin(angle)
            
            # Ensure rectangle stays within bounds
            Y_Coordinate = max(0, min(Y_Coordinate, dispH_py - rectangle_height))
        
        # Draw rectangle on pyCamera
        frame_py = cv2.rectangle(frame_py, (int(X_Coordinate), int(Y_Coordinate)),
                                 (int(X_Coordinate + rectangle_width), int(Y_Coordinate + rectangle_height)),
                                 (255, 0, 255), 3)
        cv2.imshow('pyCamera', frame_py)
        cv2.moveWindow('pyCamera', 0, 550)
        
        # Draw rectangle on Logitech Camera
        frame_log = cv2.rectangle(frame_log, (int(X_Coordinate), int(Y_Coordinate)),
                                  (int(X_Coordinate + rectangle_width), int(Y_Coordinate + rectangle_height)),
                                  (255, 0, 255), 3)
        cv2.imshow('Logitech Camera', frame_log)
        cv2.moveWindow('Logitech Camera', 0, 0)
        
        # Add a small delay to control frame rate
        time.sleep(0.03)
    
    # Check for 'q' key to quit the program
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cam.release()
cam_log.release()
cv2.destroyAllWindows()

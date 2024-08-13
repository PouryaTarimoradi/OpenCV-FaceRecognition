import cv2
import time
import math
import numpy as np

print(cv2.__version__)

X_Coordinate = 0
Y_Coordinate = 0
rectangle_width = 100
rectangle_height = 100
dispW = 640
dispH = 480
flip = 2

# Initialize movement vector
angle = math.radians(80)  # Start at 80 degrees
speed = 5
dx = speed * math.cos(angle)
dy = speed * math.sin(angle)

# Camera setup
# Uncomment the appropriate lines for your camera

# For NVIDIA Jetson (pyCamera):
#camSet = f'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method={flip} ! video/x-raw, width={dispW}, height={dispH}, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam = cv2.VideoCapture(camSet)

# For Logitech camera:
#cam = cv2.VideoCapture(1)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

def reflect(dx, dy, normal_x, normal_y):
    dot_product = dx * normal_x + dy * normal_y
    reflection_x = dx - 2 * dot_product * normal_x
    reflection_y = dy - 2 * dot_product * normal_y
    return reflection_x, reflection_y

while True:
    ret, frame = cam.read()
    
    if ret:
        # Convert frame to grayscale
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Convert grayscale back to BGR (but still grayscale)
        frame_gray = cv2.cvtColor(frame_gray, cv2.COLOR_GRAY2BGR)
        
        # Update position
        X_Coordinate += dx
        Y_Coordinate += dy
        
        # Check for collisions with edges
        if X_Coordinate <= 0 or X_Coordinate >= dispW - rectangle_width:
            normal_x = -1 if X_Coordinate <= 0 else 1
            normal_y = 0
            dx, dy = reflect(dx, dy, normal_x, normal_y)
            angle = math.atan2(dy, dx)
            angle += math.radians(70)  # Add 70 degrees
            dx = speed * math.cos(angle)
            dy = speed * math.sin(angle)
            X_Coordinate = max(0, min(X_Coordinate, dispW - rectangle_width))
        
        if Y_Coordinate <= 0 or Y_Coordinate >= dispH - rectangle_height:
            normal_x = 0
            normal_y = -1 if Y_Coordinate <= 0 else 1
            dx, dy = reflect(dx, dy, normal_x, normal_y)
            angle = math.atan2(dy, dx)
            angle += math.radians(70)  # Add 70 degrees
            dx = speed * math.cos(angle)
            dy = speed * math.sin(angle)
            Y_Coordinate = max(0, min(Y_Coordinate, dispH - rectangle_height))
        
        # Create a mask for the rectangle
        mask = np.zeros(frame.shape[:2], dtype=np.uint8)
        cv2.rectangle(mask, (int(X_Coordinate), int(Y_Coordinate)),
                      (int(X_Coordinate + rectangle_width), int(Y_Coordinate + rectangle_height)), 255, -1)
        
        # Copy the colored rectangle from the original frame to the grayscale frame
        frame_gray[mask == 255] = frame[mask == 255]
        
        # Draw rectangle border
        cv2.rectangle(frame_gray, (int(X_Coordinate), int(Y_Coordinate)),
                      (int(X_Coordinate + rectangle_width), int(Y_Coordinate + rectangle_height)),
                      (255, 0, 255), 3)
        
        cv2.imshow('Camera', frame_gray)
        cv2.moveWindow('Camera', 0, 0)
        
        # Add a small delay
        time.sleep(0.03)
    
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

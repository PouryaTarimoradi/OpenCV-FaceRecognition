# Contour Code Explanation for TrackingObjectByContour.py

Let's break down the contour-related code in the script:

```python
contours, _ = cv2.findContours(FGMaskComp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

for cnt in contours:
    area = cv2.contourArea(cnt)
    (x, y, w, h) = cv2.boundingRect(cnt)
    if area >= 50:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 3)
```

## 1. Finding Contours

```python
contours, _ = cv2.findContours(FGMaskComp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```

- `cv2.findContours()` is used to detect contours in the `FGMaskComp` image.
- `FGMaskComp` is the composite foreground mask created earlier in the script by combining two color range masks.
- `cv2.RETR_EXTERNAL` specifies that only the outermost contours should be retrieved.
- `cv2.CHAIN_APPROX_SIMPLE` compresses horizontal, vertical, and diagonal segments, keeping only their end points.

## 2. Sorting Contours

```python
contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
```

- This line sorts the detected contours based on their area in descending order.
- `cv2.contourArea(x)` calculates the area of each contour.
- The `reverse=True` argument ensures that larger contours come first in the list.

## 3. Processing Contours

```python
for cnt in contours:
    area = cv2.contourArea(cnt)
    (x, y, w, h) = cv2.boundingRect(cnt)
    if area >= 50:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 3)
```

This loop processes each contour:

- `area = cv2.contourArea(cnt)`: Calculates the area of the current contour.
- `(x, y, w, h) = cv2.boundingRect(cnt)`: Computes the bounding rectangle of the contour.
  - `x, y`: Coordinates of the top-left corner of the rectangle.
  - `w, h`: Width and height of the rectangle.
- `if area >= 50:`: Filters out small contours, potentially reducing noise.
- `cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 3)`: Draws a blue rectangle around the contour if its area is 50 pixels or larger.
  - `(255,0,0)`: Color of the rectangle (blue in BGR format).
  - `3`: Thickness of the rectangle border.

## Key Points

1. The script uses contours to identify and track objects based on their shape in the binary mask.
2. Contours are sorted by area, prioritizing larger objects.
3. Small contours (area < 50 pixels) are ignored, which can help reduce false positives.
4. Instead of drawing the actual contours, the script draws bounding rectangles around them.

## Potential Modifications

1. To draw the contours instead of rectangles, you could replace the `cv2.rectangle()` line with:
   ```python
   cv2.drawContours(frame, [cnt], 0, (255,0,0), 3)
   ```

2. To adjust the minimum area for contour detection, modify the value in the if statement:
   ```python
   if area >= 100:  # Changed from 50 to 100
   ```


These modifications would allow for different ways of visualizing or filtering the detected objects based on the contours.

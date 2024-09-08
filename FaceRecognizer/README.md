# Face Recognition Project

This project demonstrates real-time face recognition using the `face_recognition` library and OpenCV. It can identify known faces in images and label them accordingly.

## Project Overview

This script performs the following tasks:
1. Loads known faces and encodes them
2. Loads a test image with unknown faces
3. Detects and encodes faces in the test image
4. Compares the encodings to identify known faces
5. Draws bounding boxes and labels around recognized faces
6. Displays the result

## Key Components

* `face_recognition` library for face detection and encoding
* OpenCV for image processing and display
* Pre-loaded known faces for comparison

## Face Encoding and Recognition

### Loading and Encoding Known Faces

```python
Albert_face = face_recognition.load_image_file("/home/pourya/Desktop/pyPro/Face_Recognizer/demoImages/Known/Albert Einstein.jpeg")
AlbertEncode = face_recognition.face_encodings(Albert_face)[0]
```

This code loads an image of Albert Einstein and creates a face encoding. Similar lines follow for Marie Curie and Nikola Tesla.

- `load_image_file()`: Loads an image file into a numpy array
- `face_encodings()`: Generates a 128-dimensional face encoding for each face in the image

### Storing Encodings and Names

```python
Encodings = [AlbertEncode, marie_curieEncode, Nicola_TeslaEncode]
Names = ["Albert Einstein", "Marie Curie ", "Nicola Tesla"]
```

These lists store the encodings and corresponding names of known faces.

### Processing the Test Image

```python
testImage = face_recognition.load_image_file("/home/pourya/Desktop/pyPro/Face_Recognizer/demoImages/Unknown/8.jpeg")
facePosition = face_recognition.face_locations(testImage)
allEncodings = face_recognition.face_encodings(testImage, facePosition)
```

This code loads the test image, detects face locations, and generates encodings for each detected face.

- `face_locations()`: Finds all face locations in an image
- `face_encodings()`: Generates encodings for the detected faces

### Face Recognition and Labeling

```python
for (top, right, bottom, left), face_encodings in zip(facePosition, allEncodings):
    name = "Unknown Person"
    matches = face_recognition.compare_faces(Encodings, face_encodings)
    if True in matches:
        first_match_index = matches.index(True)
        name = Names[first_match_index]
    cv2.rectangle(testImage, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.putText(testImage, name, (left, top-6), font, 0.3, (0, 255, 255), 1)
```

This loop processes each detected face:
- `compare_faces()`: Compares the encoding of the detected face against all known face encodings
- If a match is found, the corresponding name is assigned
- A rectangle is drawn around the face and the name is added as a label

## Usage

1. Ensure `face_recognition` and OpenCV are installed.
2. Place known face images in the specified directory.
3. Update the file paths for known faces and the test image.
4. Run the script:
   ```
   python face_recognition_script.py
   ```
5. The script will display the test image with recognized faces labeled.
6. Press 'q' to exit the program.

## Customization

You can modify:
- Paths to known face images and test images
- The list of known faces and their corresponding names
- Display parameters (e.g., window size, font, colors)


## Contributing

Feel free to fork this project, submit pull requests, or send suggestions to improve the code. All contributions are welcome!

## License

This project is open source and available under the MIT License.

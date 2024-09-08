import face_recognition
import cv2 
print(cv2.__version__)
Albert_face=face_recognition.load_image_file("/home/pourya/Desktop/pyPro/Face_Recognizer/demoImages/Known/Albert Einstein.jpeg")
AlbertEncode=face_recognition.face_encodings(Albert_face)[0]

marie_curie_face=face_recognition.load_image_file("/home/pourya/Desktop/pyPro/Face_Recognizer/demoImages/Known/marie curie.jpeg")
marie_curieEncode=face_recognition.face_encodings(marie_curie_face)[0]

Nicola_Tesla_face=face_recognition.load_image_file("/home/pourya/Desktop/pyPro/Face_Recognizer/demoImages/Known/Nicola Tesla.jpeg")
Nicola_TeslaEncode=face_recognition.face_encodings(Nicola_Tesla_face)[0]

Encodings=[AlbertEncode,marie_curieEncode,Nicola_TeslaEncode]

Names=["Albert Einstein", "Marie Curie ", "Nicola Tesla"]

font=cv2.FONT_HERSHEY_SIMPLEX
testImage= face_recognition.load_image_file("/home/pourya/Desktop/pyPro/Face_Recognizer/demoImages/Unknown/8.jpeg")

facePosition= face_recognition.face_locations(testImage)
allEncodings=face_recognition.face_encodings(testImage,facePosition)

testImage=cv2.cvtColor(testImage,cv2.COLOR_RGB2BGR)

for (top,right,bottom,left), face_encodings in zip(facePosition, allEncodings):
    name="Unknown Person"
    matches=face_recognition.compare_faces(Encodings,face_encodings)
    if True in matches:
        first_match_index=matches.index(True)
        name=Names[first_match_index]
    cv2.rectangle(testImage,(left,top),(right,bottom), (0,0,255), 2)
    cv2.putText(testImage,name,(left,top-6),font,0.3,(0,255,255),1)

testImage=cv2.resize(testImage, (620, 480))
cv2.imshow("myWindow", testImage)
cv2.moveWindow("myWindow", 0,0)
if cv2.waitKey(0)==ord("q"):
    cv2.destroyAllWindows()

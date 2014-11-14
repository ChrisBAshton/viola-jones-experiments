import cv2
import sys

faces_count = 0

cascade_dir = "/usr/local/Cellar/opencv/2.4.9/share/OpenCV/haarcascades/"
face_cascade = cv2.CascadeClassifier(cascade_dir + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cascade_dir + "haarcascade_eye.xml")

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    eyes = eye_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )  

    # Draw a rectangle around the eyes
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    # Overlay face count and tally
    faces_count += len(faces)
    cv2.putText(frame, 'Faces: ' + str(len(faces)) + ', Tally: ' + str(faces_count), (200, 700), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)
    
    # Display the resulting frame
    cv2.imshow('Face detection using Haar', frame)

    if cv2.waitKey(10) == 27:
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
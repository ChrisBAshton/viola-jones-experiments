import cv2
import sys

cascade_dir = "/usr/local/Cellar/opencv/2.4.9/share/OpenCV/haarcascades/"
face_cascade = cv2.CascadeClassifier(cascade_dir + "haarcascade_frontalface_default.xml")
portrait_cascade = cv2.CascadeClassifier(cascade_dir + "haarcascade_profileface.xml")

filename = '/Users/ashton/Desktop/training-originals/0008_005.jpg'

# read image and resize it
image = cv2.imread(filename)
reduce_by = 4
width,height = image.shape[1]/reduce_by,image.shape[0]/reduce_by
image = cv2.resize(image, (width, height))

# detect face(s)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)
portraits = portrait_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
for (x, y, w, h) in portraits:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)

# show image until pressing Esc
cv2.imshow('Face detection using Haar', image)
while True:
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
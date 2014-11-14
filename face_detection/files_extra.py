import cv2
import sys
import os

cascade_dir = "/usr/local/Cellar/opencv/2.4.9/share/OpenCV/haarcascades/"
face_cascade = cv2.CascadeClassifier(cascade_dir + "haarcascade_frontalface_default.xml")
portrait_cascade = cv2.CascadeClassifier(cascade_dir + "haarcascade_profileface.xml")

indir = '/Users/ashton/Desktop/training-originals'

images_with_faces    = []
images_without_faces = []

for root, dirs, filenames in os.walk(indir):
    for filename in filenames:
        
        img_path = os.path.join(root, filename)

        print "Examining... " + img_path
        
        if not img_path.endswith('.jpg'):
            print "Not a valid image. Skipping..."
        else:

            image = cv2.imread(img_path)

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

            if len(faces) > 0 or len(portraits) > 0:
                images_with_faces.append(img_path)
            else:
                images_without_faces.append(img_path)

print "IMAGES WITH FACES"
print images_with_faces

print "IMAGES WITHOUT FACES"
print images_without_faces
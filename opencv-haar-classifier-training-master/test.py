import cv2
import sys
import os

face_cascade = '/usr/local/Cellar/opencv/2.4.9/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml'
personal_cascade = '/Users/ashton/Downloads/cascade.xml'
cascade = cv2.CascadeClassifier(personal_cascade)

indir = '/Users/ashton/Downloads/train_classifier/output'
outdir = '/Users/ashton/Downloads/train_classifier/output_with_detected_bodies/'

images_with_faces    = []
images_without_faces = []

for root, dirs, filenames in os.walk(indir):
    for filename in filenames:
        
        img_path = os.path.join(root, filename)

        print "Opening " + img_path

        # read image and resize it
        image = cv2.imread(img_path)

        # detect face(s)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=7,
            minSize=(40, 80),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        if len(faces) > 0:
            # Draw a rectangle around the bodies
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            images_with_faces.append(img_path)
            cv2.imwrite(outdir + filename, image)
        else:
            images_without_faces.append(img_path)

print "IMAGES WITH FACES"
print images_with_faces

print "IMAGES WITHOUT FACES"
print images_without_faces
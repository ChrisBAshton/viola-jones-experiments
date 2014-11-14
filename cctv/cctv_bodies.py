import cv2
import os

cascade_dir = "/usr/local/Cellar/opencv/2.4.9/share/OpenCV/haarcascades/"
body_cascade = cv2.CascadeClassifier(cascade_dir + "haarcascade_fullbody.xml")

indir  = '/Users/ashton/Dropbox/uni/year_4/cs341_10_computer_vision/assignment/code/cctv'
outdir = '/Users/ashton/Dropbox/uni/year_4/cs341_10_computer_vision/assignment/code/cctv_processed'

images_with_bodies    = []
images_without_bodies = []

for root, dirs, filenames in os.walk(indir):
    for filename in filenames:
        
        img_path = os.path.join(root, filename)

        print "Examining... " + img_path
        
        # open image and detect bodies
        image = cv2.imread(img_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        bodies = body_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=3,
            minSize=(10, 10),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        # Draw a rectangle around the bodies
        for (x, y, w, h) in bodies:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # write to file in the appropriate directory
        if len(bodies) > 0:
            write_filename = outdir + '/contain_bodies/'
            images_with_bodies.append(img_path)
        else:
            write_filename = outdir + '/do_not_contain_bodies/'
            images_without_bodies.append(img_path)

        write_filename = write_filename + filename

        cv2.imwrite(write_filename, image)

print "Images with bodies: " + str(len(images_with_bodies))
print "Images without bodies: " + str(len(images_without_bodies))
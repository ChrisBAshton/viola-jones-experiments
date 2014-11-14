# Viola-Jones algorithm exploration

This repository contains experiments etc from my Viola Jones algorithm exploration for a CS34110: Computer Vision assignment. It is a bit of an unstructured mess, but is proof of work and a useful repository of content. Thankfully, we're marked on our scientific report rather than our code (which in this repo, was very rushed).

## CCTV

Contains randomly sourced CCTV images from Google image search. /inputs contains the input images, /cctv_processed contains directories of the positive and negative outputs when run against the OpenCV full frontal face classifier and the OpenCV body classifier. This shows the effectiveness of the classifiers and the algorithm in 'real world' CCTV conditions.

## face_detection

References images sourced from the Massachusetts Institute of Technology and to the Center for Biological and Computational Learning's "Face Recognition Database", available at http://cbcl.mit.edu/software-datasets/heisele/facerecognition-database.html.

The Python files are my own code, used to quickly check the effectiveness of the OpenCV face detection classifier on images taken in controlled conditions.

## opencv-haar-classifier-training-master

Is a clone of the repo of the same name, which I used at various points to help me train my own classifier.

## train_classifier

I used https://www.youtube.com/watch?v=MlMerr9H9xw CCTV footage to try and train my own classifier tailored to a specific store. A command from the top level commands.txt generated an image from the video every 5 seconds. I then manually went in and cropped the positives (bodies) and negatives (everything else) from those outputted images. I used these to train my classifier.

There is some cross over between this directory and the opencv-haar-classifier-training-master directory. In the latter, positives.txt and negatives.txt refer to the positive and negative images in train_classifier.

I use the bin/createsamples.pl script to make vector samples from my positives (went into /samples directory, not git commited), but the OpenCV traincascade program only takes one vector, so I used the Open Source mergevec.py script to merge my /samples directory into one, single positives.vec.

myvecfile.vec was a vector file produced by the OpenCV makesample program, given a list of positive images. It didn't work very successfully, and contributed to classifier_1 which couldn't detect anything at all.

## classifier_1/2

Contains my completed cascade classifiers. (both were generated using different parameters and hence work differently)

The output of classifier 2 is in `train_classifier/output_with_detected_bodies`. For comparison, I also have `output_with_detected_faces` with OpenCV's own face cascade classifier, so you can compare effectiveness.
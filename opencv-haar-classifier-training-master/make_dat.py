from PIL import Image # `brew install homebrew/python/pillow`

current_dir  = '/Users/ashton/Downloads/opencv-haar-classifier-training-master/'
images = []

with open(current_dir + 'positives.txt', 'rU') as f:
  for line in f:
    line = line.rstrip() # remove newline
    images.append(line)

with open(current_dir + 'info.dat', 'a') as myfile:
    for image in images:
        im = Image.open(image) # (width,height) tuple
        image = image[2:]
        myfile.write(image + ' ' + '1' + ' ' + str(im.size[0] - 1) + ' ' + str(im.size[1] - 1) + ' ' + str(1) + ' ' + str(1) + '\n')
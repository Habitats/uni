import numpy as np
from PIL import Image

# USING PIL + numpy
def negative(image):
    out = image.point(lambda p : abs(p - 255))
    return out

# helper functions
def imageToNumpy(im):
    return np.array(im)

def numpyToImage(im):
    return Image.fromarray(im)

def saveImg(im, name):
    im.save(name)

# returns np array
def readImageFromUrl(path):
    # it is preferred to use pyl.imread(): http://bit.ly/Xv7tT1
#    return numpyToImage(pyl.imread(path))
    return Image.open(path)

# this image is in float64
#path = "test.png"

# these are uint8?
path = "test2.png"
#path = "dog.jpg"
#path = "stinkbug.png"

# load the image from file
image = readImageFromUrl(path)

# convert to numpy
arr = imageToNumpy(image)

# convert to PIL image
image = numpyToImage(arr)
image = negative(image)

# save the image
saveImg(image, "tits.png")

# display the image in the default image viewer
image.show()

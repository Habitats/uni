import numpy as np
from PIL import Image

# helper functions
def imageToNumpy(im):
    return np.array(im)

def numpyToImage(im):
    return Image.fromarray(im)

def saveImg(im, name):
    im.save(name)

# returns np array
def readImageFromUrl(path):
    return Image.open(path)

def saltAndPepperNoise(image, density):
    noise = np.random.randint(2, size = (image.shape[0], image.shape[1], 3))
    image *= noise
    return image

path = "stinkbug.png"
density = 2

# load the image from file
image = readImageFromUrl(path)
arr = imageToNumpy(image)

# apply salt & pepper noise
arr = saltAndPepperNoise(arr, density)

# convert to PIL image
image = numpyToImage(arr)

# save the image
saveImg(image, "salt_and_pepper.png")

# display the image in the default image viewer
image.show()

import numpy as np
import pylab as pyl
from PIL import Image

# helper functions
def imageToNumpy(im):
    return np.array(im)

def numpyToImage(im):
    return Image.fromarray(im)

def saveImg(im, name):
    im.save(name)

# returns np array
def readImageFromPath(path):
    return imageToNumpy(Image.open(path))

def normalize(numpy_array):
    low, high = numpy_array.min(), numpy_array.max()
    func = lambda X: (X - low) / float(high - low)
    return func(numpy_array)

def correctDistortion():
    imgOne = readImageFromPath("testimages/disturbed_potw1144a.png")
    imgTwo = readImageFromPath("testimages/flatfieldimage.png")

    imgTwo = normalize(imgTwo)

    # correct the distortion
    img = imgOne / imgTwo

    # convert back to image object
    img = numpyToImage(img)

    # save before showing
    img.show()
    saveImg(img , "disturbed_potw1144a_fix.png")

correctDistortion()




import numpy as np
import pylab as pyl
from scipy import misc

def readImageFromPath(path):
    imgArr = pyl.imread(path)
    return imgArr

def renderImg(imgArr):
    imgplot = pyl.imshow(imgArr)
    imgplot.set_interpolation("nearest")
    imgplot.set_cmap("gray")

def saveImage(filename, img):
    pyl.axis("off")
    pyl.xlim(0, img.shape[0]); pyl.ylim(img.shape[1], 0)
    misc.imsave(filename + ".png", img)

def correctDistortion():
    imgOne = readImageFromPath("testimages/disturbed_potw1144a.png")
    imgTwo = readImageFromPath("testimages/flatfieldimage.png")

    img = imgOne * imgTwo
    renderImg(img)
    saveImage("disturbed_potw1144a_fix", img)
    img2 = imgOne * (1. / imgTwo)
    renderImg(img2)
    saveImage("disturbed_potw1144a_fix2", img2)


    # save before showing

#    pyl.show()

correctDistortion()




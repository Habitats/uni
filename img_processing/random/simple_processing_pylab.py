import pylab as pyl
from scipy import misc

# USING PYLAB + malplotlib
def readImageFromPath(path):
    imgArr = pyl.imread(path)
    return imgArr

def renderImg(imgArr):
    imgplot = pyl.imshow(imgArr)
    imgplot.set_interpolation("nearest")
    imgplot.set_cmap("gray")

def saveImage(filename, img):
    pyl.axis("off")
    pyl.xlim(0, img.shape[0])
    pyl.ylim(img.shape[1], 0)
    misc.imsave(filename + ".png", img)

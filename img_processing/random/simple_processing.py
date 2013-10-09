import matplotlib.pyplot as plt
import numpy as np
import pylab as pyl


def plotImg(imgArr):
    # plot image
    imgplot = plt.imshow(imgArr, origin = "upper")
    return imgplot


def monochromeInverted(imgArr):
    # get dimensions
    width = imgArr.shape[0]
    height = imgArr.shape[1]

    imgGray = np.zeros((width, height), dtype = np.double)
    imgGray[1:width, 1:height] = imgArr[1:width, 1:height, 1]

    # process
    tmp = 512 * np.ones((width, height), dtype = np.double)
    myout = tmp - imgGray

    # plot monchrome
    imgplot = plt.imshow(myout)
    imgplot.set_cmap("gray")
    imgplot.set_interpolation("nearest")

    return imgplot
    # plt.savefig("output.png")

def luminosity(imgArr):
    lumImg = imgArr[:, :, 0]
    imgplot = plt.imshow(lumImg)
    return imgplot

imgPath = "test.png"
#imgPath = "4x4.png"
#imgPath = "stinkbug.png"

# read
imgArr = pyl.imread(imgPath)

# process
#imgplot = plotImg(imgArr)
#imgplot = luminosity(imgArr)
imgplot = monochromeInverted(imgArr)

# display the plot
#plt.show()
imgArr.show()

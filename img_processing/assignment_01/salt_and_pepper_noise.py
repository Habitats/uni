from PIL import Image
import numpy as np

image = Image.open("testimages/mandrill.png")
density = 1

def saltnpepper(image, density = density):
    """
    Add black and white noise to an image.
    1. generate a matrix which dictates which pixels to manipulate.
    2. set the pixels we do not intent to manupulate to 0
    3. apply the noise to our pixels
    4. normalize the values to [0,255] # this is not required
    5. return an image
    
    Note: 
    We multiply by 510 because 0.5*510 = 255. This will ensure that
    the salt and pepper noise actually becomes of of the extremas
    """
    noise = density * np.random.randn(*image.size)
    np.putmask(noise, np.logical_and(noise < 0.5, noise > -0.5), 0)

    return Image.fromarray(np.asarray(image) + 510 * noise)
#end saltnpepper

image = saltnpepper(image)
image.convert("RGB").save("mandrill_noise_%i.png" % density)
image.show()

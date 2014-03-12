from numpy import *

def identity():
    return array([1, 0, 0, 0,
                  0, 1, 0, 0,
                  0, 0, 1, 0,
                  0, 0, 0, 1], float32)

def rotate(a, axis, m = identity()):
    a *= 1 / 180. * pi
    if axis == 'x':
        rotationMatrix = array([1, 0 , 0 , 0,
                                0, cos(a), -sin(a), 0,
                                0, sin(a), cos(a), 0,
                                0, 0, 0, 1], float32)
    elif axis == 'y':
        rotationMatrix = array([cos(a), 0, sin(a), 0,
                                0, 1, 0, 0,
                                - sin(a), 0, cos(a), 0,
                                0, 0, 0, 1], float32)
    elif axis == 'z':
        rotationMatrix = array([cos(a), -sin(a), 0, 0,
                                sin(a), cos(a), 0, 0,
                                0, 0, 1, 0,
                                0, 0, 0, 1], float32)

    return dot(m.reshape(4, 4), rotationMatrix.reshape(4, 4)).reshape(-1)

def translate(x, y, z, m = identity()):
    translationMatrix = array([1, 0, 0, x,
                               0, 1, 0, y,
                               0, 0, 1, z,
                               0, 0, 0, 1], float32)
    return dot(m.reshape(4, 4), translationMatrix.reshape(4, 4)).reshape(-1)

def scale(x, y, z, m = identity()):
    scalingMatrix = array([x, 0, 0, 0,
                           0, y, 0, 0,
                           0, 0, z, 0,
                           0, 0, 0, 1], float32)
    return dot(m.reshape(4, 4), scalingMatrix.reshape(4, 4)).reshape(-1)


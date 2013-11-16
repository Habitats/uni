from PIL import Image

"""
reads a file with the following format:

    projectimages/sweetsA01.png
    1-13-37:70:29-40,197:40,242:42,118:42,157:44,75:86,121:101,161:117,201:142,247:145,71:147,113:149,156:149,199
    2-8-175:14:8-184,71:224,71:234,202:235,154:235,248:236,112:263,73:298,72
    3-13-144:161:196-331,151:331,197:331,244:333,74:333,114:366,111:384,149:396,193:425,68:425,109:425,240:427,149:429,193
    4-11-217:173:12-470,70:471,109:475,150:476,192:476,237:517,238:557,108:558,66:560,192:560,237:562,152

and creates a dictionary from it 
"""

def readData(filename):
    f = open(filename, 'r')
    data = []
    image = Image.open(f.readline().rstrip())
    for line in f:
        index, numSim, rgb, pairs = line.split('-')
        pairs = pairs.split(':')
        rgb = rgb.split(':')
        color = {
             'index':index,
             'numSim': numSim,
             'rgb': rgb,
             'pairs' : pairs
        }
        data.append(color)

    f.close()
    return data, image

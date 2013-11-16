from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()
from OpenGLContext.arrays import *
# OpenGL.GL contains the standard OpenGL functions
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
from PIL import Image

def readData(filename):
    f = open(filename, 'r')
    data = []
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
    return data

class Context(BaseContext):

    image = None
    data = None

    # whatever happens when the program is idle
    def OnIdle(self,):
        self.triggerRedraw(1)
        return 1

    # Render function is called after the OpenGL setup code is done
    def Render(self, mode):

        def move(x, y , z = -29.0, color = None, image = self.image):
            glLoadIdentity()
            lx = -23 + x / 12.
            ly = +17 + -y / 12.
            glTranslatef(lx, ly, z);

        # speed = duration for each rotation
        def rotate(speed):
            glRotated(time.time() % (speed) / speed * -360, 0, 1, 0)

        def color(r, g, b):
            glColor3f(r / 255., g / 255., b / 255.)

        def square(r = 255, g = 255, b = 255, w = 1, h = 1, t = 1):
            # [0, 1]

            glBegin(GL_QUADS)
            glColor3f(r / 255, g / 255, b / 255)

            # back
            glVertex3f(-w, h, -t)
            glVertex3f(w, h, -t)
            glVertex3f(w, -h, -t)
            glVertex3f(-w, -h, -t)

            # front
            glVertex3f(-w, h, t)
            glVertex3f(w, h, t)
            glVertex3f(w, -h, t)
            glVertex3f(-w, -h, t)

            # right
            glVertex3f(w, -h, t)
            glVertex3f(w, h, t)
            glVertex3f(w, h, -t)
            glVertex3f(w, -h, -t)

            # top
            glVertex3f(-w, h, -t)
            glVertex3f(w, h, -t)
            glVertex3f(w, h, t)
            glVertex3f(-w, h, t)

            # left
            glVertex3f(-w, h, t)
            glVertex3f(-w, -h, t)
            glVertex3f(-w, -h, -t)
            glVertex3f(-w, h, -t)

            # bottom
            glVertex3f(w, -h, t)
            glVertex3f(w, -h, -t)
            glVertex3f(-w, -h, -t)
            glVertex3f(-w, -h, t)

            glEnd()


        def triangle(r = 255, g = 255, b = 255, w = 1, h = 1, t = 1):

            glBegin(GL_TRIANGLES)
            glColor3f(r / 255, g / 255, b / 255)

            # backface
            glVertex3f(0, h, -t)
            glVertex3f(-w, -h, -t)
            glVertex3f(w, -h, -t)

            # frontface
            glVertex3f(0, h, t)
            glVertex3f(-w, -h, t)
            glVertex3f(w, -h, t)

            glEnd()

            glBegin(GL_QUADS)

            # right
            glVertex3f(w, -h, t)
            glVertex3f(0, h, t)
            glVertex3f(0, h, -t)
            glVertex3f(w, -h, -t)

            # left
            glVertex3f(0, h, t)
            glVertex3f(-w, -h, t)
            glVertex3f(-w, -h, -t)
            glVertex3f(0, h, -t)

            # bottom
            glVertex3f(w, -h, t)
            glVertex3f(w, -h, -t)
            glVertex3f(-w, -h, -t)
            glVertex3f(-w, -h, t)

            glEnd()

        def number3d(n, x, y):

            y -= 20

            d = 0.5
            dy = 6
            dx = 4

            w, h, t = 0.1, 0.1, 0.05

            if n == 0:
                # top
                move(x, y + dy)
                square(r, g, b, w * 4, h, t)

                # bottom
                move(x, y - dy)
                square(r, g, b, w * 4, h, t)

                # right
                move(x + dx, y)
                square(r, g, b, w , h * 4, t)

                # left
                move(x - dx, y)
                square(r, g, b, w , h * 4, t)
            elif n == 1:
                move(x - dx / 3, y - dy)
                square(r, g, b, w * 1.5  , h, t)

                # mid vert
                move(x, y)
                square(r, g, b, w, h * 4, t)

                move(x, y + dy)
                square(r, g, b, w * 2 , h, t)
            elif n == 2:
                move(x, y + dy)
                square(r, g, b, w * 4, h, t)

                move(x, y - dy)
                square(r, g, b, w * 4, h, t)

                # mid hor
                move(x, y)
                square(r, g, b, w * 4, h, t)

                move(x - dx, y + dy / 2)
                square(r, g, b, w , h * 2, t)

                move(x + dx, y - dy / 2)
                square(r, g, b, w , h * 2, t)

            elif n == 3:
                move(x + dx, y)
                square(r, g, b, w , h * 4, t)

                move(x, y - dy)
                square(r, g, b, w * 4, h, t)

                move(x, y + dy)
                square(r, g, b, w * 4, h, t)

                move(x + dx / 2, y)
                square(r, g, b, w * 2 , h , t)

            elif n == 4:
                move(x + dx, y)
                square(r, g, b, w , h * 4, t)

                move(x, y)
                square(r, g, b, w * 4 , h , t)

                move(x - dx, y - dy / 2)
                square(r, g, b, w , h * 2, t)

            elif n == 5:
                move(x, y + dy)
                square(r, g, b, w * 4, h, t)

                move(x, y - dy)
                square(r, g, b, w * 4, h, t)

                move(x, y)
                square(r, g, b, w * 4, h, t)

                move(x - dx, y - dy / 2)
                square(r, g, b, w , h * 2, t)

                move(x + dx, y + dy / 2)
                square(r, g, b, w , h * 2, t)

            elif n == 6:
                move(x, y + dy)
                square(r, g, b, w * 4, h, t)

                move(x, y - dy)
                square(r, g, b, w * 4, h, t)

                move(x, y)
                square(r, g, b, w * 4, h, t)

                move(x - dx, y)
                square(r, g, b, w , h * 4, t)

                move(x + dx, y + dy / 2)
                square(r, g, b, w , h * 2, t)

            elif n == 7:
                # top
                move(x + dx / 3, y - dy)
                square(r, g, b, w * 3, h, t)

                # right
                move(x + dx, y)
                square(r, g, b, w , h * 4, t)

                move(x + dx , y)
                square(r, g, b, w * 3, h, t)

            elif n == 8:

                # top
                move(x, y + dy)
                square(r, g, b, w * 4, h, t)

                # bottom
                move(x, y - dy)
                square(r, g, b, w * 4, h, t)

                # right
                move(x + dx, y)
                square(r, g, b, w , h * 4, t)

                # left
                move(x - dx, y)
                square(r, g, b, w , h * 4, t)

                # mid hor
                move(x, y)
                square(r, g, b, w * 4, h, t)

            elif n == 9:
                move(x, y + dy)
                square(r, g, b, w * 4, h, t)

                move(x, y - dy)
                square(r, g, b, w * 4, h, t)

                move(x, y)
                square(r, g, b, w * 4, h, t)

                move(x + dx, y)
                square(r, g, b, w , h * 4, t)

                move(x - dx, y - dy / 2)
                square(r, g, b, w , h * 2, t)

        def number2d(n):
            glBegin(GL_QUADS)
            #-#-#
            # # #
            # # #
            if n in [0, 2, 3, 5, 6, 7, 8, 9]:
                glVertex3f(-1, 1, 0)
                glVertex3f(1, 1, 0)
                glVertex3f(1, 0.6, 0)
                glVertex3f(-1, 0.6, 0)

            # # #
            #-#-#
            # # #
            if n in [2, 3, 4, 5, 6, 8, 9]:
                glVertex3f(-1, 0.2, 0)
                glVertex3f(1, 0.2, 0)
                glVertex3f(1, -0.2, 0)
                glVertex3f(-1, -0.2, 0)

            # # #
            # # #
            #-#-#
            if n in [0, 2, 3, 5, 6, 8, 9]:
                glVertex3f(-1, -1, 0)
                glVertex3f(-1, -0.6, 0)
                glVertex3f(1, -0.6, 0)
                glVertex3f(1, -1, 0)

            #|# #
            #|# #
            # # #
            if n in [0, 5, 4, 6, 8, 9]:
                glVertex3f(-1, 1, 0)
                glVertex3f(-0.5, 1, 0)
                glVertex3f(-0.5, 0, 0)
                glVertex3f(-1, 0, 0)

            # #|#
            # #|#
            # # #
            if n in [0, 2, 3, 4, 5, 6, 7, 8, 9]:
                glVertex3f(1, 1, 0)
                glVertex3f(0.5, 1, 0)
                glVertex3f(0.5, 0, 0)
                glVertex3f(1, 0, 0)

            # # #
            #|# #
            #|# #
            if n in [0, 2, 6, 8]:
                glVertex3f(-1, 0, 0)
                glVertex3f(-0.5, 0, 0)
                glVertex3f(-0.5, -1, 0)
                glVertex3f(-1, -1, 0)

            # # #
            # #|#
            # #|#
            if n in [0, 3, 4, 5, 6, 7, 8, 9]:
                glVertex3f(1, 0, 0)
                glVertex3f(0.5, 0, 0)
                glVertex3f(0.5, -1, 0)
                glVertex3f(1, -1, 0)

            # | #
            # | #
            # | #
            if n in [1]:
                glVertex3f(0.5, 1, 0)
                glVertex3f(0.5, -1, 0)
                glVertex3f(-0.5, -1, 0)
                glVertex3f(-0.5, 1, 0)
            glEnd()


        """Render the scene geometry"""
        BaseContext.Render(self, mode)
        glDisable(GL_LIGHTING)
        glDisable(GL_CULL_FACE)

        for i in self.data:
            r, g, b = i.get('rgb')
            r, g, b = double(r), double(g), double(b)
            numSim = int(i.get('numSim'))
            for pair in i.get('pairs'):
                x, y = pair.split(',')
                move(double(x), double(y))
                glScalef(0.8, 0.5, 0.5)
                rotate(3)
                width, height, thickness, shape = i.get('pref')

                if shape == 0:
                    triangle(r, g, b, width , height, thickness)
                elif shape == 1:
                    square(r, g, b, width , height, thickness)

                d = -2
                for j in str(numSim):
                    move(double(x) + d, double(y) - 15)
#                    number3d(int(j), double(x) + d, double(y))
                    glScalef(0.1, 0.3, 0)
                    rotate(-5)
                    number2d(int(j))
                    d += 3
#                glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, 2);


    def OnInit(self):
        self.image = Image.open('projectimages/sweetsA02.png')
        self.data = readData('circles.txt')

        def constructShapes(data):
            for i in data:
                width = random.random() * 0.5 + 0.5
                height = random.random() * 0.5 + 0.5
                thickness = random.random() * 0.5 + 0.5

                shape = random.randint(0, 2)
                i['pref'] = [width, height, thickness, shape]

        constructShapes(self.data)


        width, height = self.image.size
        glutReshapeWindow(width, height)
        None

if __name__ == "__main__":
    Context.ContextMainLoop()


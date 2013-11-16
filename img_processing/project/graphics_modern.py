from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()
from OpenGLContext.arrays import *
from OpenGL.GL import shaders
# OpenGL.GL contains the standard OpenGL functions
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGLContext.events.timer import Timer
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
    light_location = (0, 10, 5)
    def Render(self, mode = 0):

        def move(x, y , z = -29.0, color = None, image = self.image):
            glLoadIdentity()
            lx = -23 + x / 12.
            ly = +17 + -y / 12.
            glTranslatef(lx, ly, z);
            rotate(5)

        # speed = duration for each rotation
        def rotate(speed):
            glRotate(time.time() % (speed) / speed * -360, 1, 1, 0)

        def color(r, g, b):
            glColor3f(r / 255., g / 255., b / 255.)

        """Render the scene geometry"""
        BaseContext.Render(self, mode)
        glUseProgram(self.program)
        glUniform3fv(self.light_uniform_loc, 1, self.light_location)
        glDisable(GL_LIGHTING)
        glDisable(GL_CULL_FACE)
        glFrontFace(GL_CW)

        for i in self.data:
            r, g, b = i.get('rgb')
            r, g, b = double(r), double(g), double(b)
            numSim = int(i.get('numSim'))

            for pair in i.get('pairs'):
                x, y = pair.split(',')
                move(double(x), double(y))
                rotate(5)

                glutSolidTeapot(1)
#                glutSolidCube(1)
#                if shape == 0:
#                elif shape == 1:

#                d = -8
#                for j in str(numSim):
#                    number(int(j), double(x) + d, double(y))
#                    d += 15p


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

        self.program = shaders.compileProgram(
            shaders.compileShader(
                '''
                varying vec3 normal;
                void main() {
                    normal = gl_NormalMatrix * gl_Normal;
                    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
                }
                ''',
                GL_VERTEX_SHADER,
            ),
            shaders.compileShader(
                '''
                uniform vec3 light_location;
                varying vec3 normal;
                void main() {
                    float intensity;
                    vec4 color;
                    vec3 n = normalize(normal);
                    vec3 l = normalize(light_location).xyz;
                
                    // quantize to 5 steps (0, .25, .5, .75 and 1)
                    intensity = (floor(dot(l, n) * 4.0) + 1.0)/4.0;
                    color = vec4(intensity*0.5, intensity*0.5, intensity*0.5,
                        intensity*0.5);
                
                    gl_FragColor = color;
                }
                ''',
                GL_FRAGMENT_SHADER,
            ),
        )
        self.light_uniform_loc = glGetUniformLocation(self.program, 'light_location')

        width, height = self.image.size
        glutReshapeWindow(width, height)


if __name__ == "__main__":
    Context.ContextMainLoop()


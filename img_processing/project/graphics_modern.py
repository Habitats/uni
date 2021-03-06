from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()
from OpenGLContext.arrays import *
from OpenGL.GL import shaders
# OpenGL.GL contains the standard OpenGL functions
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGLContext.events.timer import Timer

# non openGL stuff
import time
from PIL import Image
from fetchData import *
from pyglm import *


vertexShader = '''
varying vec3 normal;
uniform mat4 mMatrix;
uniform mat4 vMatrix;
uniform mat4 pMatrix;
varying vec4 pos;

void main() {
    normal = gl_NormalMatrix * gl_Normal;
    pos = gl_ModelViewProjectionMatrix * pMatrix * vMatrix * mMatrix* gl_Vertex;
    gl_Position = pos;
    gl_Position = vec4(pos[0]+1.,pos[1]+1.,pos[2]+1., pos[3]+1.);
}
'''

fragmentShader = '''
uniform vec3 light_location;
varying vec3 normal;
void main() {
    float intensity;
    vec4 color;
    vec3 n = normalize(normal);
    vec3 l = normalize(light_location).xyz;

    // quantize to 5 steps (0, .25, .5, .75 and 1)
    intensity = (floor(dot(l, n) * 4.0) + 1.0)/4.0;
    color = vec4(intensity*1.0, intensity*0.5, intensity*0.5, intensity*1.0);

    gl_FragColor = color;
}
'''

class Context(BaseContext):

    image = None
    data = None

    # whatever happens when the program is idle
    def OnIdle(self,):
        self.triggerRedraw(1)
        return 1

    # Render function is called after the OpenGL setup code is done
#    rot = identity()
    light_location = (0, 10, 5)
    mMatrix = identity()
    vMatrix = identity()
    pMatrix = identity()

    def Render(self, mode = 0):

        BaseContext.Render(self, mode)
        glUseProgram(self.program)
#
        # animate
#        self.mMatrix = translate(5, 2, 0)
        speed = 5
        self.mMatrix = identity()
#        self.mMatrix = translate(1, 0, 0, self.mMatrix)
#        self.mMatrix = scale(3, 4, 1, self.mMatrix)
#        self.mMatrix = rotate(40 , 'z', self.mMatrix)
#        self.mMatrix = rotate(time.time() % (speed) / speed * -360 , 'x', self.mMatrix)
        self.mMatrix = translate(1, 0, 0, self.mMatrix)
        v = array([0, 0, 0, 0])
        print v.dot(self.mMatrix.reshape(4, 4))
        speed = 5

#        speed *= 0.5
#        self.mMatrix = rotate(time.time() % (speed) / speed * -360   , 'z', self.mMatrix)
#        speed *= 4
#        self.mMatrix = rotate(time.time() % (speed) / speed * -360  , 'y', self.mMatrix)
#        self.vMatrix = translate(0, 1, 0)

#        speed = 10
#        self.vMatrix = rotate(time.time() % (speed) / speed * -360 , 'x')
#        self.mMatrix = rotate(90, 'z')


        # modify the light location in the shader, number of matrices,
        glUniform3fv(self.light_uniform_loc, 1, self.light_location)
        glUniformMatrix4fv(self.mMatrixId, 1, GL_FALSE, self.mMatrix)
        glUniformMatrix4fv(self.vMatrixId, 1, GL_FALSE, self.vMatrix)
        glUniformMatrix4fv(self.pMatrixId, 1, GL_FALSE, self.pMatrix)
        glUniform4fv(self.vPos, 1, v)

        glDisable(GL_LIGHTING)
        glDisable(GL_CULL_FACE)
        glFrontFace(GL_CW)


        glutSolidCube(1)



    def OnInit(self):
        self.data, self.image = readData('circles.txt')

        def constructShapes(data):
            for i in data:
                width = random.random() * 0.5 + 0.5
                height = random.random() * 0.5 + 0.5
                thickness = random.random() * 0.5 + 0.5

                shape = random.randint(0, 2)
                i['pref'] = [width, height, thickness, shape]

        constructShapes(self.data)

        self.program = shaders.compileProgram(
            shaders.compileShader(vertexShader, GL_VERTEX_SHADER),
            shaders.compileShader(fragmentShader, GL_FRAGMENT_SHADER),
        )
        # get the location of the uniform variable from the shader (if the variable isn't used, -1 is returned
        self.vMatrixId = glGetUniformLocation(self.program, 'vMatrix')
        self.mMatrixId = glGetUniformLocation(self.program, 'mMatrix')
        self.pMatrixId = glGetUniformLocation(self.program, 'pMatrix')
        self.vPos = glGetUniformLocation(self.program, 'pos')
        self.light_uniform_loc = glGetUniformLocation(self.program, 'light_location')

        width, height = self.image.size
        glutReshapeWindow(width, height)


if __name__ == "__main__":
    Context.ContextMainLoop()


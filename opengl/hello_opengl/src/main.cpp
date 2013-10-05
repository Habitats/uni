#include <GL/glut.h>
#include <GL/freeglut.h>
#include <stdio.h>
#include "visuals.h"

//Main program

int main(int argc, char **argv) {

	glutInit(&argc, argv);
// enables you to select between RGB or palette model, single or double 
// buffering etc (to avoid flickering)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE);

	//Configure window position in X and Y cords from upper left corner
	glutInitWindowPosition(50, 25);

	//Configure Window Size
	glutInitWindowSize(480, 480);

	//Create Window with title “Hello OpenGL”
	glutCreateWindow("Hello OpenGL");

// initializes the state of our “openGL-world”
	Setup();

	//Call to the drawing function
	glutDisplayFunc(Render);

	//Call to the resize/reshape function whenever the windows changes size
	glutReshapeFunc(Resize);

	// Loop require by OpenGL
	glutMainLoop();
	return 0;
}


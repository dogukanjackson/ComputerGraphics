# CENG 487 Assignment3 by
# DoğukanÇiftçi
# StudentId: 230201071
# December 2021
from vec3d import *
from ToriEcubeParser import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from mat3d import *
from primitives import *
from oobject import *


# Number of the glut window.
checker=0
subdivision=0
window = 0
xaxis=0
yaxis=0
zaxis=0

rotated=0

# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
    global primitive
    glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
    glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
    glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
    filename=sys.argv[1]
    Parser=parser(filename)
    primitive=Parser.parse()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()					# Reset The Projection Matrix
										# Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)



# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
	if Height == 0:						# Prevent A Divide By Zero If The Window Is Too Small
		Height = 1

	glViewport(0, 0, Width, Height)		# Reset The Current Viewport And Perspective Transformation
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)


# The main drawing function.
def DrawGLScene():
    global primitive,rotated,subdivision, checker,xaxis,yaxis
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);	# Clear The Screen And The Depth Buffer
    glLoadIdentity();				# Reset The View
    glTranslatef(0,0.0,-7.0);	# Move Left And Into The Screen
    glPolygonMode(GL_FRONT, GL_LINE)
    glPolygonMode(GL_BACK, GL_LINE)
    glBegin(GL_QUADS)

    glColor3f(1,0,0)
    if xaxis!=0 or yaxis!=0:
        primitive.rotate(xaxis,yaxis,0)
        xaxis=0
        yaxis=0
    if checker<subdivision:
        primitive.subdivision()
    elif checker>subdivision:
        primitive.merge()
    checker=subdivision
    for square in primitive.squares:
        
        for vertex in square.vertices:
            #print(vertex.x)
            glVertex3f(vertex.x,vertex.y,vertex.z)
    glEnd();	
    text="Number of subdivision is:"+str(subdivision)
    glRasterPos2f(-2.5, -2.5)
    for i in range(len(text)):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(text[i]))


	#  since this is double buffered, swap the buffers to display what just got drawn.
    glutSwapBuffers()

    
# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
def keyPressed(key, x, y):
    global subdivision
	# If escape is pressed, kill everything.
	# ord() is needed to get the keycode
    if ord(key)== 27:
		# Escape key = 27
        tLeaveMainLoop()
    elif key == '+'.encode("utf-8"):
        subdivision+=1
    elif key == '-'.encode("utf-8"):
        if subdivision>0:
            subdivision-=1
def rotateKey(key, x, y):
    global xaxis,yaxis
    if key==GLUT_KEY_UP:
        xaxis=-0.1
    if key==GLUT_KEY_DOWN:
        xaxis=0.1
    if key==GLUT_KEY_RIGHT:
        yaxis=0.1
    if key==GLUT_KEY_LEFT:
        yaxis=-0.1

def main():
    global window
    glutInit(sys.argv)


	# Select type of Display mode:
	#  Double buffer
	#  RGBA color
	#  Alpha components supported
	#  Depth buffer
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    

	# get a 640 x 480 window
    glutInitWindowSize(640, 480)

	# the window starts at the upper left corner of the screen
    glutInitWindowPosition(0, 0)

	# Okay, like the C version we retain the window id to use when closing, but for those of you new
	# to Python (like myself), remember this assignment would make the variable local and not global
	# if it weren't for the global declaration at the start of main.
    window = glutCreateWindow("230201071 assignment3")

   	# Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
	# set the function pointer and invoke a function to actually register the callback, otherwise it
	# would be very much like the C version of the code.
    glutDisplayFunc(DrawGLScene)

	# Uncomment this line to get full screen.
	# glutFullScreen()

	# When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)

	# Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)

	# Register the function called when the keyboard is pressed.
    glutKeyboardFunc(keyPressed)

    glutSpecialFunc(rotateKey)
	# Initialize our window.
    InitGL(640, 480)

	# Start Event Processing Engine
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print ("Hit ESC key to quit.\nPress \"+\" to increase subdivision\nPress \"-\" to decrease subdivision.")
main()
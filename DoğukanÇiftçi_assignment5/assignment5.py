# CENG 487 Assignment5 by
# DoğukanÇiftçi
# StudentId: 230201071
# January 2022
import sys
import numpy
import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from numpy import *

from vector import *
from matrix import *
from shapes import *
from camera import *
from scene import *
from view import *
from shader import *

glutInit(sys.argv)
   
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
   
glutInitWindowSize(640, 480)
glutInitWindowPosition(200, 200)
   
window = glutCreateWindow("230201071 Assignment5")
# create camera
camera = Camera()
camera.createView( 	Point3f(0.0, 0.0, 10.0), \
					Point3f(0.0, 0.0, 0.0), \
					Vector3f(0.0, 1.0, 0.0) )
camera.setNear(1)
camera.setFar(1000)

# create View
view = View(camera)

# init scene
scene = Scene()
view.setScene(scene)
vertexcode = Shader('vertexshader.glsl',GL_VERTEX_SHADER)
fragmentcode=Shader('fragmentshader.glsl',GL_FRAGMENT_SHADER)
triangle = Shape('triangle', [[0.5, 0.5, 0.0, 1.0],[0.5, 0.0, 0.0, 1.0,],[0.0, 0.0, 0.0, 1.0]],
[[0, 1, 2]],
 GL_TRIANGLES,
[[0.0, 0.0, 1.0, 1.0]])
triangle.createProgram([vertexcode.shaderID, fragmentcode.shaderID])

scene.add(triangle)
def main():
	global view


	# define callbacks
	glutDisplayFunc( view.display )
	glutIdleFunc( view.idleFunction )
	glutReshapeFunc( view.resizeView )
	glutKeyboardFunc( view.keyPressed )
	glutSpecialFunc( view.specialKeyPressed )
	glutMouseFunc( view.mousePressed )
	glutMotionFunc( view.mouseMove )

	# Initialize our window
	width = 640
	height = 480
	glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
	glDepthFunc(GL_LEQUAL)				# The Type Of Depth Test To Do
	glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
	#glEnable(GL_LINE_SMOOTH)			# Enable line antialiasing
	glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading



	# Start Event Processing Engine
	glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print("Hit ESC key to quit.")
main()


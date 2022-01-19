# CENG 487 Assignment5 by
# DoğukanÇiftçi
# StudentId: 230201071
# January 2022
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from vector import *
from matrix import *
from shapes import *
from scene import *
from defs import *

class Event:
    def __init__(self):
        self.x = -1
        self.y = -1
        self.button = -1
        self.state = -1
        self.altPressed = False


class View:
    def __init__(self, camera, scene = None):
        self.camera = camera
        self.scene = scene
        self.bgColor = ColorRGBA(0.15, 0.15, 0.15, 1.0)
        self.cameraIsMoving = False
        self.objectAnimOn = False
        self.event = Event()
        self.mouseX = -1
        self.mouseY = -1


    def display(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT)
        for i in self.scene.nodes:
        # use our program
            elementSize = numpy.dtype(numpy.float32).itemsize
            glUseProgram(i.programID)
            vertexDim=4
            # reset our vertex buffer
            glBindBuffer(GL_ARRAY_BUFFER, i.VBO)
            glEnableVertexAttribArray(0)
            glVertexAttribPointer(0, vertexDim, GL_FLOAT, GL_FALSE, 0, None)
            offset = i.nVertices * vertexDim * elementSize
            glEnableVertexAttribArray(1)
            glVertexAttribPointer(1, vertexDim, GL_FLOAT, GL_FALSE, offset, None)
            glDrawArrays(i.drawStyle, 0, i.nVertices)
    
        # reset to defaults
        glDisableVertexAttribArray(0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glUseProgram(0)
    
        glutSwapBuffers()




    def setScene(self, scene):
        self.scene = scene


    def setObjectAnim(self, onOff):
        self.objectAnimOn = onOff


    def isObjectAnim(self):
        return self.objectAnimOn


    def setCameraIsMoving(self, onOff):
        self.cameraIsMoving = onOff


    def isCameraMoving(self):
        return self.cameraIsMoving


    # The function called whenever a key is pressed.
    def keyPressed(self, key, x, y):
        # If escape is pressed, kill everything.
        # ord() is needed to get the keycode
        if ord(key) == 27:
            # Escape key = 27
            glutLeaveMainLoop()
            return

        if key == b'f':
            self.camera.reset()
            self.draw()

        if key == b'4':
            for node in self.scene.nodes:
                if not node.fixedDrawStyle:
                    node.drawStyle = DrawStyle.WIRE
                    node.wireOnShaded = False
                    self.draw()

        if key == b'5':
            for node in self.scene.nodes:
                if not node.fixedDrawStyle:
                    node.drawStyle = DrawStyle.SMOOTH
                    node.wireOnShaded = False
                    self.draw()

        if key == b'6':
            for node in self.scene.nodes:
                if not node.fixedDrawStyle and node.drawStyle != DrawStyle.WIRE:
                    node.wireOnShaded = True
                    self.draw()


    # The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
    def resizeView(self, width, height):
        if height == 0:                        # Prevent A Divide By Zero If The Window Is Too Small
            height = 1

        glViewport(0, 0, width, height)        # Reset The Current Viewport And Perspective Transformation
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.camera.fov, float(width)/float(height), self.camera.near, self.camera.far)
        glMatrixMode(GL_MODELVIEW)


    # The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
    def specialKeyPressed(self, *args):
        if args[0] == GLUT_KEY_LEFT:
            self.camera.eye.x -= .5
            self.camera.center.x -= .5
            self.camera.computeFrame()

        if args[0] == GLUT_KEY_RIGHT:
            self.camera.eye.x += .5
            self.camera.center.x += .5
            self.camera.computeFrame()


    def mousePressed(self, button, state, x, y):
        self.event.x = x
        self.event.y = y
        self.event.state = state
        self.event.button = button

        # get status of alt key
        m = glutGetModifiers()
        self.event.altPressed = m & GLUT_ACTIVE_ALT

        self.mouseX = x
        self.mouseY = y

        if state == 0:
            if self.event.altPressed > 0:
                self.setCameraIsMoving( True )
        else:
            self.setCameraIsMoving( False )


    def mouseMove(self, x, y):
        if self.event.altPressed == False:
            return

        xSpeed = 0.02
        ySpeed = 0.02
        xOffset = (x - self.mouseX) * xSpeed
        yOffset = (y -self.mouseY) * ySpeed

        if ( self.event.button == GLUT_RIGHT_BUTTON ):
            self.camera.zoom(xOffset)
            #self.camera.roll(yOffset)
        elif ( self.event.button == GLUT_MIDDLE_BUTTON ):
            self.camera.dolly(-xOffset, yOffset, 0)
        elif ( self.event.button == GLUT_LEFT_BUTTON ):
            self.camera.yaw(xOffset)
            self.camera.pitch(yOffset)
            #self.camera.dollyCamera(-xOffset, yOffset, 0)

        # store last positions
        self.mouseX = x
        self.mouseY = y

        # remember this point
        self.event.x = x
        self.event.y = y


    # The main drawing function
    def idleFunction(self):
        if self.isObjectAnim() or self.isCameraMoving():
            self.display()
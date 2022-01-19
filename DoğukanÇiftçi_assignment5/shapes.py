# CENG 487 Assignment5 by
# DoğukanÇiftçi
# StudentId: 230201071
# January 2022
import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from math import pi,sin,cos,sqrt,acos
from vector import *
from matrix import *
from numpy import *

class Shape:
    def __init__(self, name, vertices, faces,drawStyle,colors):
        self.vertices = vertices
        self.edges = []
        self.faces = faces
        self.colors = colors
        self.obj2World = Matrix()
        self.drawStyle = drawStyle
        self.wireOnShaded = False
        self.wireWidth = 2
        self.name = name
        self.fixedDrawStyle = False
        self.wireColor = ColorRGBA(0.7, 1.0, 0.0, 1.0)
        self.wireOnShadedColor = ColorRGBA(1.0, 1.0, 1.0, 1.0)


    def setDrawStyle(self, style):
        self.drawStyle = style


    def setWireColor(self, r, g, b, a):
        self.wireColor = ColorRGBA(r, g, b, a)


    def setWireWidth(self, width):
        self.wireWidth = width



    def Translate(self, x, y, z):
        translate = Matrix.T(x, y, z)
        self.obj2World = self.obj2World.product(translate)
    def createProgram(self,shaderList):
        programID = glCreateProgram()
        for shader in shaderList:
            glAttachShader(programID, shader)
            glLinkProgram(programID)
            status = glGetProgramiv(programID, GL_LINK_STATUS)
            if status == GL_FALSE:
                strInfoLog = glGetProgramInfoLog(programID)
                print(b"Linker failure: \n" + strInfoLog)
                
        for shaderID in shaderList:
            glDetachShader(programID, shaderID)
        for shader in shaderList:
            glDeleteShader(shader)
        self.programID=programID
        self.initVertexBuffer()
    def initVertexBuffer(self):
        self.VBO = glGenBuffers(1)
    
        # set array buffer to our ID
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
    
        # set data
        bufferData = self.setBufferData()
        glBufferData( # PyOpenGL allows for the omission of the size parameter
            GL_ARRAY_BUFFER,
            bufferData,
            GL_STATIC_DRAW
        )
    
        # reset array buffer
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        
    def setBufferData(self):
        data = []
        color = []
        nVertices = 0

        for i in range(len(self.faces)):
            for j in self.faces[i]:
                nVertices = nVertices+1
                data.extend(self.vertices[j])
                color.extend(self.colors[i])
        self.nVertices =nVertices
        return numpy.concatenate((data, color), dtype = numpy.float32)






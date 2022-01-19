# CENG 487 Assignment5 by
# DoğukanÇiftçi
# StudentId: 230201071
# January 2022
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
class Shader:
    def __init__(self,filename,shadertype):
        self.filename=filename
        self.shadertype=shadertype
        self.createShader()
    def createShader(self):
        shaderID = glCreateShader(self.shadertype)
        glShaderSource(shaderID, self.fileread())
        glCompileShader(shaderID)
    
        status = None
        glGetShaderiv(shaderID, GL_COMPILE_STATUS, status)
        if status == GL_FALSE:
            # Note that getting the error log is much simpler in Python than in C/C++
            # and does not require explicit handling of the string buffer
            strInfoLog = glGetShaderInfoLog(shaderID)
            strShaderType = ""
            if shaderType is GL_VERTEX_SHADER:
                strShaderType = "vertex"
            elif shaderType is GL_GEOMETRY_SHADER:
                strShaderType = "geometry"
            elif shaderType is GL_FRAGMENT_SHADER:
                strShaderType = "fragment"
    
            print(b"Compilation failure for " + strShaderType + b" shader:\n" + strInfoLog)
    
        self.shaderID=shaderID
    def fileread(self):
        inside=open(self.filename,'r')
        mystr=inside.read()
        return mystr
        
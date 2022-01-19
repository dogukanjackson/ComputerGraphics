# CENG 487 Assignment5 by
# DoğukanÇiftçi
# StudentId: 230201071
# January 2022
#version 330
layout(location = 0) in vec4 vertexPosition;
layout(location = 1) in vec4 vertexcolor;
out vec4 fragcolor;
void main()
{
   gl_Position = vertexPosition;
   fragcolor = vertexcolor;
}
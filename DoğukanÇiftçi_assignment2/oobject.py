# CENG 487 Assignment1 by
# DoğukanÇiftçi
# StudentId: 230201071
# October 2021

class oobject :
    def __init__(self, position,vertices,matrix_stack):
        self.position = position
        self.vertices = vertices
        self.matrix_stack=matrix_stack
        
    def applyMatrixToVertices(self, mat3d):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = mat3d.multiply(vertex)
            
    def applyMatrixStack(self):
        for matrix in self.matrix_stack:
            self.applyMatrixToVertices(matrix)
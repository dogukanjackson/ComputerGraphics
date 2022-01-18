from vec3d import*
from oobject import*
from mat3d import*
class cube:
    def __init__(self):
        self.squares=[]
        self.oldSquares=[]
    def addSquare(self,square):
        self.squares.append(square)
    def clone(self,square):
        new_vertices=[]
        for vertex in square.vertices:
            new_vertices.append(vertex)
        return oobject(0,new_vertices,[])
    
    def createcube(self,square):
        #self.squares.append(self.clone(square))
        s1=self.clone(square)
        s1.matrix_stack.append(mat3d().rotation_zx_matrix(1.5707963268))
        s1.applyMatrixStack()
        self.squares.append(s1)
        s2=self.clone(square)
        s2.matrix_stack.append(mat3d().rotation_zx_matrix(3.1415926536))
        s2.applyMatrixStack()
        self.squares.append(s2)
        s3=self.clone(square)
        s3.matrix_stack.append(mat3d().rotation_zx_matrix(4.7123889804))
        s3.applyMatrixStack()
        self.squares.append(s3)
        s4=self.clone(square)
        s4.matrix_stack.append(mat3d().rotation_zx_matrix(6.2831853072))
        s4.applyMatrixStack()
        self.squares.append(s4)
        v1=self.squares[0].vertices[0]
        v2=self.squares[1].vertices[0]
        v3=self.squares[2].vertices[0]
        v4=self.squares[3].vertices[0]
        
        v5=self.squares[0].vertices[2]
        v6=self.squares[1].vertices[2]
        v7=self.squares[2].vertices[2]
        v8=self.squares[3].vertices[2]
        
        s5=oobject(0,[v1,v2,v3,v4],[])
        s6=oobject(0,[v5,v6,v7,v8],[])
        self.squares.append(s5)
        self.squares.append(s6)
    def middlePointOfEdge(self,v1,v2):
        v3=vec3d(round((v1.x+v2.x)/2,4),round((v1.y+v2.y)/2,4),round((v1.z+v2.z)/2,4),1)
        return v3
    def middleOfSquare(self,square):
        v1=vec3d(square.vertices[0].x,square.vertices[0].y,square.vertices[0].z,0)
        v2=vec3d(square.vertices[1].x,square.vertices[1].y,square.vertices[1].z,0)
        v3=vec3d(square.vertices[2].x,square.vertices[2].y,square.vertices[2].z,0)
        v4=vec3d(square.vertices[3].x,square.vertices[3].y,square.vertices[3].z,0)
        v5=self.middlePointOfEdge(v1,v2)
        v6=self.middlePointOfEdge(v3,v4)
        Vm=self.middlePointOfEdge(v5,v6)
        return Vm

    def merge(self): 
        self.squares=self.oldSquares.pop()
    def subdivision(self):
        newSquares=[]
        for square in self.squares:
            v1=square.vertices[0]
            v2=square.vertices[1]
            v3=square.vertices[2]
            v4=square.vertices[3]
            Mp=self.middleOfSquare(square)
            M1=self.middlePointOfEdge(v1,v2)
            M2=self.middlePointOfEdge(v2,v3)
            M3=self.middlePointOfEdge(v3,v4)
            M4=self.middlePointOfEdge(v4,v1)
            Ns1=oobject(0,[v1,M1,Mp,M4],[])
            Ns2=oobject(0,[M1,v2,M2,Mp],[])
            Ns3=oobject(0,[M4,Mp,M3,v4],[])
            Ns4=oobject(0,[Mp,M2,v3,M3],[])
            newSquares.append(Ns1)
            newSquares.append(Ns2)
            newSquares.append(Ns3)
            newSquares.append(Ns4)
        self.oldSquares.append(self.squares)
        self.squares=newSquares



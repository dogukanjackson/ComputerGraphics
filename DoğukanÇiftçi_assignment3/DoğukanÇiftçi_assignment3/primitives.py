# CENG 487 Assignment3 by
# DoğukanÇiftçi
# StudentId: 230201071
# December 2021
from vec3d import*
from oobject import*
from mat3d import*
class primitives:
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
    def rotate(self,x,y,z):
        for s in self.squares:
            s.rotate(x,y,z)
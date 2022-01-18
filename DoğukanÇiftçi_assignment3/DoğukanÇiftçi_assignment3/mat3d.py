import copy
import math  
from vec3d import vec3d


class mat3d :
    def __init__(self, matrix=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]):
        self.matrix = matrix
        
        
    def multiply(self,vec3dd):
        return vec3d(
            vec3d(self.matrix[0][0],self.matrix[0][1],self.matrix[0][2],self.matrix[0][3]).dot_product(vec3dd), 
            vec3d(self.matrix[1][0],self.matrix[1][1],self.matrix[1][2],self.matrix[1][3]).dot_product(vec3dd), 
            vec3d(self.matrix[2][0],self.matrix[2][1],self.matrix[2][2],self.matrix[2][3]).dot_product(vec3dd), 
            vec3d(self.matrix[3][0],self.matrix[3][1],self.matrix[3][2],self.matrix[3][3]).dot_product(vec3dd))
        
        
    def scaling_matrix(self,scale_x,scale_y,scale_z):
        self.matrix[0][0] = self.matrix[0][0]*scale_x
        self.matrix[1][1] = self.matrix[1][1]*scale_y
        self.matrix[2][2] = self.matrix[2][2]*scale_z
        return self.matrix
    
    def translating_matrix(self,x,y,z):
        matrix = copy.deepcopy(self.matrix)
        matrix[0][3] = self.matrix[0][3]+x
        matrix[1][3] = self.matrix[1][3]+y
        matrix[2][3] = self.matrix[2][3]+z
        return mat3d(matrix)

    def rotate_x(self,angle):
        sin = math.sin(angle*math.pi/180)
        cos = math.cos(angle*math.pi/180)
        
        self.matrix[1][1]=cos
        self.matrix[1][2]=-sin
        self.matrix[2][1]=sin
        self.matrix[2][2]=cos
        return self
    
    def rotate_y(self,angle):
        sin = math.sin(angle*math.pi/180)
        cos = math.cos(angle*math.pi/180)
        
        self.matrix[0][0]=cos
        self.matrix[0][2]=sin
        self.matrix[2][0]=-sin
        self.matrix[2][2]=cos
        return self
    
    def rotate_z(self,angle):
        sin = math.sin(angle*math.pi/180)
        cos = math.cos(angle*math.pi/180)
        
        self.matrix[0][0]=cos
        self.matrix[0][1]=-sin
        self.matrix[1][0]=sin
        self.matrix[1][1]=cos
        return self
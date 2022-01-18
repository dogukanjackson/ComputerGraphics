import math  


class vec3d :
    def __init__(self, x, y,z,w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    
    def Magnitute(self):
        return (self.x**2+self.y**2+self.z**2)**0.5

    def addition(self,other_vec3d):
        x = self.x+other_vec3d.x
        y = self.x+other_vec3d.y
        z = self.x+other_vec3d.z
        w =self.w
        return vec3d(x, y, z, w)
    
    def scalar_multp(self,value):
        x = self.x*value
        y = self.x*value
        z = self.x*value
        w =self.w*value
        return vec3d(x, y, z, w)
    
    def dot_product(self,other_vec3d):
        return self.x*other_vec3d.x + self.y*other_vec3d.y +self.z*other_vec3d.z+ self.w*other_vec3d.w    
    
    def cross_product(self,other_vec3d):
        x = self.y*other_vec3d.z - self.z*other_vec3d.y
        y = self.z*other_vec3d.x - self.x*other_vec3d.z
        z = self.x*other_vec3d.y - self.y*other_vec3d.x
        w = self.w
        return vec3d(x, y, z, w)
    
    def calculate_cosQ(self,other_vec3d):
        dot_prod = self.dot_product(other_vec3d)
        return dot_prod/(self.Magnitute()*other_vec3d.Magnitute())
    
    def calculate_angle(self,other_vec3d):
        return math.acos(self.calculate_cosQ(self,other_vec3d))
    
    def calculate_projection(self,basis_vect):
        basis_vector = basis_vect.calculate_basis_vector()
        a_magnitute = self.Magnitute()
        cosQ = self.calculate_cosQ(basis_vect)
        x = a_magnitute*cosQ*basis_vector.x
        y = a_magnitute*cosQ*basis_vector.y
        z = a_magnitute*cosQ*basis_vector.z
        w = self.w
        return vec3d(x, y, z, w)
       
    def calculate_basis_vector(self):
        magnitute = self.Magnitute()
        x = self.x/magnitute
        y = self.y/magnitute
        z = self.z/magnitute
        w = self.w
        return vec3d(x, y, z, w)
    
    def to_string(self):
        return self.x,self.y,self.z,self.w
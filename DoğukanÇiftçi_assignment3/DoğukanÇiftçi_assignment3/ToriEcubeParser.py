# CENG 487 Assignment3 by
# DoğukanÇiftçi
# StudentId: 230201071
# December 2021
from vec3d import *
from oobject import *
from primitives import *
class parser:
    def __init__(self,filename):
        self.filename=filename
    def parse(self):
        
        opened=open(self.filename,'r')
        lines=opened.readlines()
        linelist=[]
        vectors=[]
        orders=[]
    
        opened.close()
        for i in lines:
            linelist.append(i.split())
        for i in linelist:
            if len(i)>0:#To avoid empty line.
                if i[0]=="v":
                    vector=vec3d(float(i[1]),float(i[2]),float(i[3]),0)
                    vectors.append(vector)
                elif i[0]=="f":
                    order=[]
                    order.append(int(i[1])-1)
                    order.append(int(i[2])-1)
                    order.append(int(i[3])-1)
                    order.append(int(i[4])-1)
                    orders.append(order)
        primitive=primitives()
        for order in orders:
            vertices=[]
            for i in order:
                vertices.append(vectors[i])
            face=oobject(0,vertices,[])
            primitive.addSquare(face)
        return primitive
"""    def __init__(self,filename):
        self.filename=filename
    first=open('tori.obj','r')
    tori=first.readlines()
    torilist=[]
    torivectors=[]
    torifaces=[]
    second=open('ecube.obj','r')
    ecube=second.readlines()
    ecubelist=[]
    ecubevectors=[]
    ecubefaces=[]
    first.close()
    second.close()
    for i in tori:
        torilist.append(i.split())
    for i in torilist:
        if len(i)>0:#To avoid empty line.
            if i[0]=="v":
                vector=vec3d(i[1],i[2],i[3],0)
                torivectors.append(vector)
            elif i[0]=="f":
                face=[]
                face.append(i[1])
                face.append(i[2])
                face.append(i[3])
                face.append(i[4])
                torifaces.append(face)
    for i in ecube:
        ecubelist.append(i.split())
    for i in ecubelist:
        if len(i)>0:#To avoid empty line.
            if i[0]=="v":
                vector=vec3d(i[1],i[2],i[3],0)
                ecubevectors.append(vector)
            elif i[0]=="f":
                face=[]
                face.append(i[1])
                face.append(i[2])
                face.append(i[3])
                face.append(i[4])
                ecubefaces.append(face)"""
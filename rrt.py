import numpy as np
import random

floorplan  = np.zeros((500 , 500))

class rrttree:
    def __init__ (self  ,x , y, nodeno , parent ):
        self.x = x 
        self.y = y 
        self.nodeno = nodeno
        self.parent = parent 
    
N = 5000
step_size = 10
threshold = 40
x_max = 600; y_max = 600

rrt = rrttree(5 , 5 , 1, 0 ) 
rrtT = {}
rrtT[rrt.nodeno]=rrt
parent=1; currnode=2

iter = 2 
def getdistance() :
    # return the min distance and the index for it. 
    # return distance  , mi 
    pass

def goalreached() :
    #check if the goal is reached return true
    
    pass 

while iter  < N :
    x_rand = np.random.uniform(0,x_max)
    y_rand = np.random.uniform(0,y_max)
    distance , mi = getdistance()

    if distance >= step_size:
        x_new = 
    
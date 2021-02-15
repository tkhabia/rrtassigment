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

rrt = rrttree(5 , 5 , 1, 0) 
rrtT = {}
rrtT[rrt.nodeno]=rrt
# parent=1; currnode=2

iter = 2 
def getdistance() :
    # return the min distance and the index for it. 
    # return distance  , mi 
    pass

def goalreached(rrtnode) :
    #check if the goal is reached from the generated node, then return true
    distance = np.sqrt((rrtnode.x-x_goal)**2 + (rrtnode.y-y_goal)**2)
    if distance <=threshold:
    	rrtgoal=rrttree(x_goal, y_goal, iter+1, iter)
    	rrtT[iter+1]=rrtgoal
    	return True
    else:
    	iter+=1
    	return False


while iter  < N :
    x_rand = np.random.uniform(0,x_max)
    y_rand = np.random.uniform(0,y_max)
    distance , mi = getdistance()

    if distance >= step_size:
        x_new = 
    
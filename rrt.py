import numpy as np
import random
import cv2 


floorplan = np.full((600, 600 , 3) , 255)

class rrttree:
    def __init__(self, x, y, nodeno, parent):
        self.x = x
        self.y = y
        self.nodeno = nodeno
        self.parent = parent


N = 5000
step_size = 10
threshold = 25
x_max = 600
y_max = 600
bias = 0.2

x_goal = 400
y_goal = 500
rrt = rrttree(5, 5, 1, 0)
floorplan =cv2.circle(floorplan , (5, 5) , 4 , (0,255 , 0),-1)
floorplan =cv2.circle(floorplan , (x_goal, y_goal) , 25 , (0,0 , 255),-1)

rrtT = {}
rrtT[rrt.nodeno] = rrt

iter = 2


def getdistance():
    # return the min distance and the index for it.
    # return distance  , parentind 
    pass


def goalreached(rrtnode):
    # check if the goal is reached from the generated node, then return true
    distance = np.sqrt((rrtnode.x-x_goal)**2 + (rrtnode.y-y_goal)**2)
    if distance <= threshold:
        rrtgoal = rrttree(x_goal, y_goal, iter+1, iter)
        rrtT[iter+1] = rrtgoal
        return True
    else:
        return False


while iter < N:
    if np.random.uniform(0, 1, 1)[0] < bias:
        x_rand = x_goal
        y_rand = y_goal
    else:
        x_rand = np.round(np.random.uniform(0, x_max))
        y_rand = np.round(np.random.uniform(0, y_max))

    distance, parentind = getdistance()

    if distance >= step_size:
        x_new = rrtT[parentind].x + \
            ((x_rand - rrtT[parentind].x)*step_size)/distance
        y_new = rrtT[parentind].y + \
            ((y_rand - rrtT[parentind].y)*step_size)/distance
    else:
        x_new = x_rand
        y_new = y_rand
    
    rrt = rrttree(x_new, y_new, iter, parentind)
    rrtT[rrt.nodeno] = rrt

    if goalreached(rrt ):
        break
    iter += 1

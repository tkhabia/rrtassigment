import numpy as np
import cv2
import matplotlib.pyplot as plt
from numpy.lib.polynomial import RankWarning
from makepath import makefloor
from combine import frames_to_video
import os 
os.system("rm holonomic/*.png")

class rrttree:
    def __init__(self, x, y, nodeno, parent , theta):
        self.x = x
        self.y = y
        self.theta = theta
        self.nodeno = nodeno
        self.parent = parent

N = 600
step_size = 18
threshold = 20
x_max = 600
y_max = 600
bias = 0.05
x_goal = 400
y_goal = 500
orientation_threshold = 10*np.pi/180
dt = 0.1
diagofrobot = 30
maxsteeing = 0.7
max_v =  30 
theta_goal = 90*np.pi/180
rrt = rrttree(50, 50, 1, 0 , 0 )
floorplan , erosion = makefloor((x_max , y_max) , diagofrobot)
floorplan = cv2.circle(floorplan, (50, 50), 8, (0, 255, 0), -1)
floorplan = cv2.circle(floorplan, (x_goal, y_goal), 8, (0, 0, 255), -1)

def goalreached(rrtnode):
    '''
    this is to check if the goal is reached. If yes then add the final edge between
    the node and the final destination.
    return true or false
    '''
    pass

def getdistance(rrtT , x_rand  , y_rand ):
    '''
    get the euclidian distance from the node which is closest to 
    the randomly selected node .
    return distance , parentind 

    '''
    pass

def drawcurve(rrt, parentind , f=0):
    """
    function to draw the curve 

    """
    pass

def checkobstical(x_new, y_new, floorplan, parentind):
    """
    function to check if there is any obstical in the 
    selected path

    """
    pass 

while iter < N:
    if np.random.uniform(0, 1, 1)[0] < bias:
        x_rand = x_goal
        y_rand = y_goal
    else:
        x_rand = np.round(np.random.uniform(0, x_max))
        y_rand = np.round(np.random.uniform(0, y_max))

    distance, parentind = getdistance(rrtT , x_rand , y_rand )

    if distance >= step_size:
        x_new = rrtT[parentind].x + \
            ((x_rand - rrtT[parentind].x)*step_size)/distance
        y_new = rrtT[parentind].y + \
            ((y_rand - rrtT[parentind].y)*step_size)/distance
    else:
        x_new = x_rand
        y_new = y_rand
    x_new = np.int(np.round(x_new))
    y_new = np.int(np.round(y_new))

    if checkobstical(x_new, y_new, erosion, parentind):
        continue

    rrt = rrttree(x_new, y_new, iter, parentind)

    rrtT[rrt.nodeno] = rrt
    drawcurve(rrt, parentind)

    if goalreached(rrt):
        break
    iter += 1
    cv2.imwrite('./non_holonomic/'  + str(iter) + '.png' , floorplan)

while(rrtT[iter].parent != 0 ):
    drawcurve(rrtT[iter] , rrtT[iter].parent , 1)
    iter = rrtT[iter].parent

# cv2.imwrite('./non_holonomic/'  + str(N+3) + '.png' , floorplan)
# frames_to_video('./non_holonomic/*.png' , './non_holonomic/holonomic.mp4' , 25)
import numpy as np
import math
import cv2
import matplotlib.pyplot as plt

floorplan = np.uint8( np.full((600, 600, 3), 255))


class rrttree:
    def __init__(self, x, y, nodeno, parent):
        self.x = x
        self.y = y
        self.nodeno = nodeno
        self.parent = parent


N = 500
step_size = 10
threshold = 25
x_max = 600
y_max = 600
bias = 0.2

x_goal = 400
y_goal = 500
rrt = rrttree(5, 5, 1, 0)
floorplan = cv2.circle(floorplan, (5, 5), 4, (0, 255, 0), -1)
floorplan = cv2.circle(floorplan, (x_goal, y_goal), 25, (0, 0, 255), -1)

rrtT = {}
rrtT[rrt.nodeno] = rrt

iter = 2


def getdistance(rrtT , x_rand  , y_rand ):
    # return the min distance and the index for it.
    # return distance  , parentind
    min_dist=(y_max*x_max)+1
    index=0
    for i in range(len(rrtT)):
        # tempnode=i
        xt,yt= rrtT[i+1].x, rrtT[i+1].y
        temp_dist=np.sqrt((x_rand-xt)**2 + (y_rand-yt)**2)
        if temp_dist<min_dist:
            min_dist=temp_dist
            index=rrtT[i+1].nodeno
    return min_dist, index


def goalreached(rrtnode):
    # check if the goal is reached from the generated node, then return true
    distance = np.sqrt((rrtnode.x-x_goal)**2 + (rrtnode.y-y_goal)**2)
    if distance <= threshold:
        rrtgoal = rrttree(x_goal, y_goal, iter+1, iter)
        rrtT[iter+1] = rrtgoal
        return True
    else:
        return False


def drawline(rrt, parentind):
    cv2.line(floorplan, (rrt.x, rrt.y),
             (rrtT[parentind].x, rrtT[parentind].x), (255, 0, 0), 1)
    cv2.circle(floorplan , (rrt.x, rrt.y) , 3 , (255 , 0 , 0 ) ,-1)


def checkobstical(x_new, y_new, floorplan, parentind):
    x_old = rrtT[parentind].x
    y_old = rrtT[parentind].y
    inc = 1 if x_old - x_new > 0 else -1
    for i in range(x_new, x_old, inc):
        yl = (y_old - y_new) * (i - x_new) / (x_old - x_new)
        # print(floorplan[i, int( math.ceil( yl))])
        if floorplan[i, int( math.ceil( yl))][0] == 0 or floorplan[i, int( math.floor( yl))][0] == 0:
            return True
    return False


while iter < N:
    # if np.random.uniform(0, 1, 1)[0] < bias:
    #     x_rand = x_goal
    #     y_rand = y_goal
    # else:
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

    if checkobstical(x_new, y_new, floorplan, parentind):
        continue

    rrt = rrttree(x_new, y_new, iter, parentind)
    rrtT[rrt.nodeno] = rrt
    drawline(rrt, parentind)
    if goalreached(rrt):
        break
    iter += 1

plt.imshow(floorplan)
plt.show()
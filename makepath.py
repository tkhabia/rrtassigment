#%% 
import numpy as np 
import cv2 
import matplotlib.pyplot as plt 


def makefloor(size , robosize): 
    floor = np.uint8( np.full (size , 255))
    # floor = cv2.copyMakeBorder(floor, 2,2,2,2,borderType=cv2.BORDER_CONSTANT)
    floor[100 : 125 , 0:  500] = 0
    floor[300 : 325 , -450 : ] = 0
    # floor[]
    
    if (robosize//2)&1:
        kernel = np.zeros((robosize//2,robosize//2,3))
        v = robosize//2 
    else :
        kernel = np.zeros((robosize//2 +1 ,1+ robosize//2,3))
        v = robosize//2 +1
    kernel = np.uint8(cv2.circle(kernel ,(v//2,v//2) , 2 , (1, 0 , 0 ),thickness=-1 )[:,:,0])
    
    erosion = cv2.erode(floor,kernel,iterations = 1)

    erosion = cv2.cvtColor(erosion , cv2.COLOR_GRAY2RGB)
    print(erosion.shape )
    return erosion 

if __name__ == "__main__":
    makefloor((600,600) , 10)

# %%

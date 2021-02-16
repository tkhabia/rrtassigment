import numpy as np 
import cv2 
import matplotlib.pyplot as plt 


def makefloor(size , robosize): 
    floor = np.uint8( np.full (size , 255))
    # floor = cv2.copyMakeBorder(floor, 2,2,2,2,borderType=cv2.BORDER_CONSTANT)
    if (robosize//2)&1:
        kernel = np.zeros((robosize//2,robosize//2,3))
        v = robosize//2 
    else :
        kernel = np.zeros((robosize//2 +1 ,1+ robosize//2,3))
        v = robosize//2 +1
    kernel = np.uint8(cv2.circle(kernel ,(v//2,v//2) , 2 , (1, 0 , 0 ),thickness=-1 )[:,:,0])
    
    erosion = cv2.erode(floor,kernel,iterations = 1)
    print(kernel)
    plt.imshow(erosion , cmap="gray")
    plt.show()
    print(floor.shape)
makefloor((600,600) , 10)
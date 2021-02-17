# python3 combine.py
import cv2
from glob import glob
import re

from matplotlib import pyplot
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

# parser = argparse.ArgumentParser(description='Converting Frames to Video and Vice Versa')
# parser.add_argument('--in', dest='input', required=True, help = "[--in \path\to\input\directory]")
# parser.add_argument('--out', dest='out', required=True, help="[--out \parh\to\output\directory]")

def frames_to_video(input_path, output_path, fps):
    '''
        Function to Concatenate given frames and fps into a video file.
        Input Arguments
        input_path  : Path to the input directory containing input frames
        output_path : Path to the output directory containing the video file
        fps         : Frames per Second of the output video
        Return
        Boolean     : True is Video written successfully, False if writing is not successful.
    '''

    # if not os.path.isdir(input_path):
    #     raise OSError(2, 'No such file or directory', input_path)
    #     return False

    # if not os.path.isdir(output_path):
    #     os.makedirs(output_path)

    image_files = sorted(glob(input_path) , key=numericalSort)
    # print(image_files)

    frames = []
    size = (600 , 600)
    for i in range(len(image_files)):
        # f = f"{input_path}/{i}.png"
        # f = f"results/{i}.png" 
        frame = cv2.imread(image_files[i])

        height, width, _ = frame.shape
        size = (width, height)
        frames.append(frame)

    video_writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for frame in frames:
        video_writer.write(frame)

    video_writer.release()
    return True

frames_to_video("results/*.png","results/abhinav.mp4", 25)
import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')
import math,datetime,functools,itertools,operator,bisect,fractions,statistics
from collections import deque,defaultdict,OrderedDict,Counter
from fractions import Fraction
from decimal import Decimal
from sys import stdout
from heapq import heappush, heappop, heapify ,_heapify_max,_heappop_max,nsmallest,nlargest
# mod=1000000007
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")
###CODE
tc = ri()
for _ in range(tc):
    
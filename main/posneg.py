# tool used to label images as positive or negative and place in correct areas for future evaluation
# check project readme for instructions


import cv2 as cv
import numpy as np
import os
from time import time
import imageio as iio

frame_skip_count = 5
frame_start = 0
video_name = '2022-03-28_22-24-34.mp4'

lastLoc = ""
if not os.path.exists('img/positive/'+str(video_name)):
    os.mkdir('img/positive/'+str(video_name))
if not os.path.exists('img/negative/'):
    os.mkdir('img/negative/')

cap = cv.VideoCapture('img/raw/'+video_name)
if (cap.isOpened() == False):
    print("Error opening video stream or file")

frameCount = 0

#skip some frames if you want to pick up where you left off
for i in range(frame_start):
    ret, frame = cap.read()
    frameCount = frameCount + 1

while(cap.isOpened()):
    ret, frame = cap.read()
    for i in range(frame_skip_count-1):
        ret, frame = cap.read()
        if ret != True:
            break
        frameCount = frameCount + 1
    

    if ret == True:

        # display the images
        cv.imshow('Unprocessed', frame)

        # press 'q' with the output window focused to exit.
        # press 'f' to save screenshot as a positive image,
        # press 'd' to save as a negative image.
        # press 'u' to delete the image saved from the last action
        # waits 1 ms every loop to process key presses
        key = cv.waitKey()
        if key == ord('q'):
            break
        elif key == ord('f'):
            lastLoc = 'img/positive/{}/{}.jpg'.format(video_name,frameCount)
            cv.imwrite(lastLoc, frame)
        elif key == ord('d'):
            lastLoc = 'img/negative/{}-{}.jpg'.format(video_name,frameCount)
            cv.imwrite(lastLoc, frame)
        elif key == ord('u'):
            os.remove(lastLoc)

    else:
        print("no more video! Frame: "+str(frameCount))
        break

    print('Done.')

cap.release()
cv.destroyAllWindows()
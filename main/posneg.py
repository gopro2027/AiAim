# tool used to label images as positive or negative and place in correct areas for future evaluation
# check project readme for instructions


import cv2 as cv
import numpy as np
import os
from time import time
import imageio as iio


loop_time = time()
program_start_time = time()
num = 0
lastLoc = ""
lastLocOrig = ""
if not os.path.exists('img/positive/'+str(program_start_time)):
    os.mkdir('img/positive/'+str(program_start_time))
while(True):

    # get an updated image of the game
    loc = "img/rand/"+str(num)+".jpg"
    while not os.path.exists(loc):
        num = num + 1
        loc = "img/rand/"+str(num)+".jpg"
    img = iio.imread(loc)

    # display the images
    cv.imshow('Unprocessed', img)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # press 'f' to save screenshot as a positive image,
    # press 'd' to save as a negative image.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey()
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('f'):
        #cv.imwrite('img/positive/{}.jpg'.format(num), img)
        os.rename(loc, 'img/positive/{}/{}.jpg'.format(program_start_time,num))
        lastLoc = 'img/positive/{}/{}.jpg'.format(program_start_time,num)
        lastLocOrig = loc
    elif key == ord('d'):
        #cv.imwrite('img/negative/{}.jpg'.format(num), img)
        os.rename(loc, 'img/negative/{}.jpg'.format(num))
        lastLoc = 'img/negative/{}.jpg'.format(num)
        lastLocOrig = loc
    elif key == ord('u'):
        os.rename(lastLoc, lastLocOrig)
        num = num - 2

    num = num + 1

print('Done.')
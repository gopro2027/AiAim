# NO LONGER USED IN THIS PROJECT!
# DREW read this and learn or something idk
#Pulls a single random image and does the object detection in it

import cv2
from matplotlib import pyplot as plt
import os, random


  
  
# Use minSize because for not 
# bothering with extra-small 
# dots that would look like STOP signs
stop_data = cv2.CascadeClassifier('misc/opencv/bin/cascade/cascade.xml')

video_name = '2022-03-28_22-21-55.mp4'
cap = cv2.VideoCapture('img/raw/'+video_name)
if (cap.isOpened() == False):
    print("Error opening video stream or file")

while(cap.isOpened()):
    ret, frame = cap.read()


    if ret == True:
        # OpenCV opens images as BRG 
        # but we want it as RGB We'll 
        # also need a grayscale version
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img_rgb = frame.copy() #cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  
        found = stop_data.detectMultiScale(img_gray, 
                                   minSize =(20, 20))
  
        # Don't do anything if there's 
        # no sign
        amount_found = len(found)
  
        if amount_found != 0:
      
            # There may be more than one
            # sign in the image
            for (x, y, width, height) in found:
          
                # We draw a green rectangle around
                # every recognized sign
                cv2.rectangle(img_rgb, (x, y), 
                      (x + height, y + width), 
                      (0, 255, 0), 1)

        cv2.imshow('Unprocessed', img_rgb)

        key = cv2.waitKey(5)
        if (key == ord('q')):
            break

cap.release()
cv2.destroyAllWindows()
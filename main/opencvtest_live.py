# this will pull a random cam and run the cascade on it real time

# check misc/opencv/training tutorial.txt for some info about training including the video

# CONTROLS:
# N: go to next traffic cam
# Q: quit (any analyzed images will not be lost by pressing q, they are already saved)
# S: Save/analyze image (opens new window)

# Controls in analyze image window:
# 1-9: select/deselect valid cars (green boxes when selected)
# Q: abort and go back to main window
# S: Save selection
# - Note about save:
#   Do not press S when there are valid cars in the picture, but you have selected 0 cars (this will save it to the negative folder and confuse the AI to think there are no cars in the image when there are valid cars) instead press Q
#   If you are unsure, press Q
#   If there are multiple valid cars, you can select 1 or more and safely press S (only the valid cars will be fed into the ai, not the unselected ones)
#   If you select nothing and click S, that means that you have a negative image, and there are no valid cars in the image and it will be put into the negative folder. This is good, and you should generate some negatives, but just make sure there are no visible cars in the negative, because that will confuse the AI because it is supposed to have none being a negative

import cv2
from matplotlib import pyplot as plt
import os, random
import sys
import subprocess
import numpy
import time
import threading
import urllib.request
import io
import uuid
import time
import signal
from os import listdir
from os.path import isfile, join

camlist = [10,11,12,13,14,15,16,17,18,19,20,21,23,25,26,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,65,67,68,69,70,71,72,73,74,75,77,78,79,80,81,84,85,86,87,88,89,90,91,92,93,96,99,101,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127]
chosenCam = str(random.choice(camlist))
program_start_time = time.time()

blackoutmode = False

#cam 72 is next to campus
VIDEO_URL = 'https://s2.ozarkstrafficoneview.com/rtplive/CAM'+chosenCam+'/playlist.m3u8'

#setup cv2 at top for use below
windowName = "Ozark"
cv2.namedWindow("Ozark",cv2.WINDOW_AUTOSIZE )
stop_data = cv2.CascadeClassifier('misc/opencv/bin/cascade/cascade.xml')



def renderimg(img):
  
    # OpenCV opens images as BRG 
    # but we want it as RGB We'll 
    # also need a grayscale version
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_rgb = img.copy()

  
    #originally used img_gray here but idk why?
    found = stop_data.detectMultiScale(img_gray, 
                                   minSize =(20, 20))
  
    amount_found = len(found)
  
    if amount_found != 0:
        for (x, y, width, height) in found:
            cv2.rectangle(img_rgb, (x, y), 
                      (x + height, y + width), 
                      (0, 0, 255), 1)
    
    cv2.imshow(windowName, img_rgb)
    return found


def writeposimage(img, found, resultarr):
    uid = uuid.uuid4().hex
    imgname = "live_"+uid+".jpg"
    count = len(resultarr)
    if count == 0:
        #put into negatives folder!
        cv2.imwrite("img/negative/"+imgname, img)
    else:
        #has data in found, put into positives folder
        folder = 'img/positive/'+str(program_start_time)
        if not os.path.exists(folder):
            os.mkdir(folder)
        
        #save the image
        cv2.imwrite(folder+"/"+imgname, img)

        thisimgdata = imgname+" "+str(count)+" "
        
        for i in resultarr:
            (x, y, width, height) = found[i]
            thisimgdata = thisimgdata + str(x) +" " + str(y) + " " + str(width)+ " " + str(height) + " "

        file1 = open(folder+"/pos.txt", "a")  # append mode
        file1.write(thisimgdata+"\n")
        file1.close()


def doImageSnapshotSubprocess(image,found):
    global blackoutmode
    resultarr = []
    while True:
        tmpimg = image.copy()
        amount_found = len(found)
  
        if amount_found != 0:
            for i in range(0,amount_found):
            #for (x, y, width, height) in found:
                (x, y, width, height) = found[i]
                color = (0, 0, 255)
                if i in resultarr:
                    color = (0, 255, 0)
                cv2.rectangle(tmpimg, (x, y), 
                  (x + height, y + width), 
                  color, 1)
                cv2.putText(tmpimg, str(chr(ord('1')+i)), (x,y+height), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        pdwin = "Please deselect if necessary"
        cv2.imshow(pdwin, tmpimg)
        
        key = cv2.waitKey()
        if key == ord('q'):
            cv2.destroyWindow(pdwin)
            time.sleep(0.1)
            return
        if cv2.getWindowProperty(pdwin,cv2.WND_PROP_VISIBLE) < 1:        
            cv2.destroyWindow(pdwin)
            time.sleep(0.1)
            return
        if key == ord('s'):
            writeposimage(image,found,resultarr)
            cv2.destroyWindow(pdwin)
            time.sleep(0.1)
            return
        if key == ord('b'):
            blackoutmode = not blackoutmode

        if key >= ord('1') and key <= ord('9'):
            val = key - ord('1')
            print(str(val))
            if val < len(found):
                if (blackoutmode == False):
                    if val in resultarr:
                        resultarr.remove(val)
                    else:
                        resultarr.append(val)
                else:
                    #blackout mode, just draw a black rectangle around the selected box
                    (x, y, width, height) = found[val]
                    color = (0, 0, 0)
                    cv2.rectangle(image, (x, y), (x + height, y + width), color, -1)

        time.sleep(0.1)


#credits to pipe: http://zulko.github.io/blog/2013/09/27/read-and-write-video-frames-in-python-using-ffmpeg/

imgx = 420
imgy = 360
pipe = 0

def startVideo(id):
    global imgx
    global imgy
    global pipe
    global VIDEO_URL

    VIDEO_URL = 'https://s2.ozarkstrafficoneview.com/rtplive/CAM'+id+'/playlist.m3u8'
    print("Cam "+str(id))
    req=urllib.request.Request(VIDEO_URL)
    with urllib.request.urlopen(req) as resp:
        data = str(resp.read()).split("\\n")
        for s in data:
            if ("RESOLUTION=" in s):
                csv = s.split(",")
                csv = csv[-1].split("=")
                csv = csv[-1].split("x")
                imgx = int(csv[0])
                imgy = int(csv[1])

    print("x and y: "+str(imgx)+" "+str(imgy))

    #it does not like high res videos so resize
    imgx = 320
    imgy = 240

    pipe = subprocess.Popen([ 'res/ffmpeg.exe', "-i", VIDEO_URL,
           "-s", str(imgx)+"x"+str(imgy),
           "-loglevel", "quiet", # no text output
           "-an",   # disable audio
           "-f", "image2pipe",
           "-pix_fmt", "rgb24",
           "-framerate", "1",
           "-vcodec", "rawvideo", "-"],
           stdin = subprocess.PIPE, stdout = subprocess.PIPE)

chosenCam = "114"
print("Randomly chosen cam: "+chosenCam)
startVideo(chosenCam)

while True:
    raw_image = pipe.stdout.read(imgx*imgy*3) # read 432*240*3 bytes (= 1 frame)
    image =  numpy.fromstring(raw_image, dtype='uint8').reshape((imgy,imgx,3))
    pipe.stdout.flush()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    found = renderimg(image)
    key = cv2.waitKey(5)
    if key == ord('q'):
        break
    if key == ord('s'):
        doImageSnapshotSubprocess(image,numpy.array(found).tolist())
    if key == ord('n'):
        pipe.kill()
        chosenCam = str(random.choice(camlist))
        startVideo(chosenCam)

    
    
    if cv2.getWindowProperty(windowName,cv2.WND_PROP_VISIBLE) < 1:        
        break

cv2.destroyAllWindows()




# depricated (do not delete may be used in future again)
# this file was used to randomize all of the downloaded images in the img/rand folder

import sys
sys.exit("Do not run unless intentional")

import os
import random

count = 0
for f1 in os.scandir("img/raw"):
    for f in os.scandir(f1.path):
        count = count + 1
print("Count: "+str(count))

randarr = random.sample(range(count), count)
count = 0
if not os.path.exists('img/rand'):
    os.mkdir('img/rand')

for f1 in os.scandir("img/raw"):
    #print(f1.name)
    cam = f1.name
    for f in os.scandir(f1.path):
        file = f.name
        #print(f.name)
        randNum = randarr[count]
        newFileLoc = "img/rand/"+str(randNum)+".jpg"
        #print("New name: "+newFileLoc)
        if os.path.exists(newFileLoc):
            print("ERROR FILE ALREADY EXISTS! "+newFileLoc)
        else:
            #os.rename("img/raw/"+cam+"/"+file, newFileLoc)
            print("Change this else statement to enable")
        count = count + 1
#os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
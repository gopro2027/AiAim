# used to count the amount of data in the result files for use in create_vec.bat and train.bat
# generates the create_vec file

import os

create_vec_contents = "opencv_createsamples.exe -info pos.txt -w 20 -h 20 -num {} -vec pos.vec\nPAUSE"

infilepos = "misc/opencv/bin/pos.txt"
infileneg = "misc/opencv/bin/neg.txt"
outfilecreatevec = "misc/opencv/bin/create_vec.bat"

poscount = 0
negcount = 0
poslinenum = 0
baddata = False
with open(infilepos, 'r') as fp:
    lines = fp.readlines()
    for line in lines:
        poslinenum = poslinenum + 1
        poscount += int(line.split(' ')[1]) # the line format is: path count data
        #if poscount == 1064:
        #    print("1063: "+str(poslinenum))
        if "0 0 0 0" in line:
            print("Bad data (\"0 0 0 0\") at line "+str(poslinenum)+"! Please fix.")
            baddata = True
if baddata == True:
    exit("Please go back to consolodatepos.py and run to see where to fix your data")

with open(infileneg, 'r') as fp:
    lines = fp.readlines()
    for line in lines:
        negcount += 1
print('positive count: '+str(poscount))
print('negative count: '+str(negcount))

with open(outfilecreatevec, 'w') as f:
    f.write(create_vec_contents.format(poscount))
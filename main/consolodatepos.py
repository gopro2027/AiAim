# used to convert the fragmentized positive image txt files into a single txt file for use during training
# check project readme for instructions

import os

outfile = "misc/opencv/bin/pos.txt"

baddata = False
data = ""
for f1 in os.scandir("img/positive"):
    if f1.is_dir:
        print(f1.path)
        if os.path.exists(f1.path+"/pos.txt"):
            with open(f1.path+"/pos.txt", 'r') as fp:
                lines = fp.readlines()
                linenum = 0
                for line in lines:
                    linenum = linenum + 1
                    if "0 0 0 0" in line:
                        print("->\tBad data (\"0 0 0 0\") at line "+str(linenum)+"! Please fix.")
                        baddata = True
                    data += '../../../'+f1.path.replace('\\','/') + '/' + line

if baddata == True:
    exit("File not written. Please fix your data and run again")

with open(outfile, 'w') as f:
    f.write(data)
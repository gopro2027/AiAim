# this file is for downloading raw data to create training data from
# Do not run it again unless we decide we need more training info on a rainy day or somehting idk, probably not ever necessary again

import sys

import os
import signal
import subprocess
import time
import threading

if not os.path.exists('img'):
    os.mkdir('img')
if not os.path.exists('img/raw'):
    os.mkdir('img/raw')

# todo:
# record videos of gameplay and parse them in here to generate data
# Aiaim
Aimbot Project

Setup:

install github desktop and clone this project (you can use this to easily update and push new updates and commits ect, also open in vs code and other things)

install visual studio code

install visual studio code extensions:

	python
	pip manager

using pip manager install:

	opencv-python
	imageio
	matplotlib

All usages of py files are labelled at the top of their files

List of bat files and usages:

	run_annotation_post.bat  - runs opencv_annotation.exe with respect to our project    - no param modification required
	create_vec.bat           - runs opencv_createsamples.exe with respect to our project - auto generated now
	train.bat                - runs opencv_traincascade.exe with respect to our project  - params may need to be modified in the file based on usage


How to run:

	Run opencvtest_live.py or opencvtest.py


Creating test data:

note: all bat scripts for opencv located in misc/opencv/bin/

only do this one person at a time to make sure you aren't moving around the same image files at the same time and make sure to push it up when you are done!


GENERATING TRAINING DATA OPTION 1:


step 1: run posneg.py in visual studio to move the files into the correct folders

	press 'd' on 'negative' images, ones that have no <object>, bad quality, or <object>s that are not going to make good training data
	press 'f' on 'positive' images, which are images where there is clear, good training data cars
	press 'u' if you made a mistake, and it will go back to the last image (does not go back further than 1)
	press 'q' to end the program
	this will put all of your negatives in the /negative folder, and all of your positives in /positive/{time}/ folder for the current session
	you can do as many positive images as you want to analyze then press q to exit and continue on to the next step
	
step 2:

	this step is for the positive files and requires the most time, and depends on how many images you chose in step 2
	run run_annotation_post.bat and select the recently generated /positive/{time}/ folder
	do the whole process of creating boxes around the <object>s as described below
	Instructions:
			"In each image you should draw a box around the objects within it that you want to be able to detect. 
			You click once to set the upper left corner, then again to set the lower right corner. 
			You'll see a red box enclosing your object. Press 'c' to confirm this selection. 
			If you don't like the box you've drawn, you can click again elsewhere to draw a different box. 
			You can also press 'd' to undo the previous confirmation. 
			When done with an image, click 'n' to move to the next one. 
			It will exit automatically when you've annotated all of the images."
	your results will be copied into the /positive/{time}/ folder as pos.txt
	

GENERATING TRAINING DATA OPTION 2:

	WILL NEED TO BE UPDATED TO USE VIDEO FIRST, IF EVEN REASONABLE

	This option is more user friendly and generates our data from live info
	Open opencvtest_live.py
	Read the controls at the top of the file on how to use it and especially for the warnings on bad data
	Run it and try generating some data

	
intermediate note:

you are done creating the new training data now for a set of images and should push up your project

GENERATING AI FILE FROM DATA:

step 1:

	run gennegfile.py 
	this will update the neg.txt files
	
step 2:

	run consolodatepos.py 
	this will create misc/opencv/bin/pos.txt

step 3:

	run countdata.py
	this will generate the create_vec.bat file with the correct number of samples and give some info in the console to help you decide the args to use in train.bat

step 4:

	run create_vec.bat
	this will turn pos.txt into pos.vec
	
step 5:

	this step is cpu intensive and takes time
	run train.bat (may need to delete old cascade folder if starting from scratch, but keep if just doing more stages)
	you may need to modify parameters inside of the command to get better results
	put good trained cascade.xml in the backup folder with some info about it and the command line ect
	

# simply generates a neg.txt file in the correct area. No further processing of negatives necessary
# check project readme for instructions

import os
# reads all the files in the /negative folder and generates neg.txt from them.
def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('misc/opencv/bin/neg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('img/negative'):
            f.write('../../../img/negative/' + filename + '\n')
            #os.rename('img/negative/'+filename,'img/negative/2022-03-28_22-21-55.mp4-'+filename)
generate_negative_description_file()


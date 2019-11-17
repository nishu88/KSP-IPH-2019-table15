import numpy as np
import cv2

from imutils import paths
import argparse
import pickle
import vptree
import cv2
import argparse
import pickle
import time
import cv2
from matplotlib import pyplot as plt


#NEW IMAGE

###############################################
path_to_trainimages= "train_images/"
trainimages=os.listdir(path_to_trainimages)

path_to_testimages="test_images/"
arrest="cropped_arrest/"
death="cropped_death/"
wanted="cropped_wanted/"

train_arrest=os.listdir(path_to_testimages+arrest)
train_death=os.listdir(path_to_testimages+death)
train_wanted=os.listdir(path_to_testimages+wanted)

folder_path="matched_pics/"

threshold=9

#################################################

print("[INFO] loading VP-Tree and hashes...")
tree = pickle.loads(open("vptreearrest.pickle", "rb").read())
hashes = pickle.loads(open("hashesarrest.pickle", "rb").read())

##################################################3


# load the input query image
count=0

for i in trainimages:
    #print("creating folder for ")
    #print(i)
    
    try:
        os.mkdir(folder_path+i)
    except:
        pass
    var1=0
    
    image = cv2.imread("train_images/"+i)
    #cv2.imshow("Query", image)
 
    # compute the hash for the query image, then convert it
    queryHash = dhash(image)
    queryHash = convert_hash(queryHash)

    print("\n[INFO] performing search...")
    start = time.time()
    results = tree.get_all_in_range(queryHash, threshold)
    results = sorted(results)
    
    #print(results,"---------------")
    
    end = time.time()
    print("[INFO] search took {} seconds".format(end - start))

    if len(results)!=0:
        for (d, h) in results:
            # grab all image paths in our dataset with the same hash
            resultPaths = hashes.get(h, [])
            print("[INFO] {} total image(s) with distance: {}, h: {}".format(len(resultPaths), d, h))

            # loop over the result paths
            for resultPath in resultPaths:
                #print(resultPath)
                result = cv2.imread(resultPath)
                cv2.imwrite(folder_path+i+"/"+str(var1)+"image.jpg",result)
                var1+=1
    else:
        print("not found")
        
    count+=1
    if count==20:
        break



    

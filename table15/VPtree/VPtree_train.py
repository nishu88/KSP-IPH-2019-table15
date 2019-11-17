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


#HASHING.PY

def dhash(image, hashSize=8):
    # convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    # resize the grayscale image, adding a single column (width) so we
    # can compute the horizontal gradient
    resized = cv2.resize(gray, (hashSize + 1, hashSize))
 
    # compute the (relative) horizontal gradient between adjacent
    # column pixels
    diff = resized[:, 1:] > resized[:, :-1]
 
    # convert the difference image to a hash
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

def convert_hash(h):
    # convert the hash to NumPy's 64-bit float and then back to
    # Python's built in int
    return int(np.array(h, dtype="float64"))

def hamming(a, b):
    # compute and return the Hamming distance between the integers
    return bin(int(a) ^ int(b)).count("1")


#ARREST
###################################################
imagePaths = list(paths.list_images("test_images/cropped_arrest"))
hashes = {}
 
# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
    # load the input image
    print("[INFO] processing image {}/{}".format(i + 1,
        len(imagePaths)))
    image = cv2.imread(imagePath)
 
    # compute the hash for the image and convert it
    h = dhash(image)
    h = convert_hash(h)
 
    # update the hashes dictionary
    l = hashes.get(h, [])
    l.append(imagePath)
    hashes[h] = l
    
print("[INFO] building VP-Tree...")
points = list(hashes.keys())
#print(points)
tree = vptree.VPTree(points, hamming)

# serialize the VP-Tree to disk
print("[INFO] serializing VP-Tree...")
f = open("vptreearrest.pickle", "wb")
f.write(pickle.dumps(tree))
f.close()
 
# serialize the hashes to dictionary
print("[INFO] serializing hashes...")
f = open("hashesarrest.pickle", "wb")
f.write(pickle.dumps(hashes))
f.close()
###################################################

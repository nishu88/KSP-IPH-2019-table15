#TESTING DATA 

import cv2
import numpy as np
import os 
import glob
from matplotlib import pyplot as plt
%matplotlib inline



#----------------------------------------------------------------
def plot_bar_x(label,no_movies):
    
    # this is for plotting purpose
    index = np.arange(len(label))
    plt.bar(index, no_movies)
    plt.xlabel('Number', fontsize=5)
    plt.ylabel('Percentage', fontsize=5)
    plt.xticks(index, label, fontsize=5, rotation=30)
    plt.title('Accuracy graph')
    plt.show()
#----------------------------------------------------------------
confidence_var= 70
#recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer1.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

count=0
accuracy=[]
image_name=[]

font = cv2.FONT_HERSHEY_SIMPLEX

id = 0

imagePaths = glob.glob('final_dataset/*/*')

for imagePath in imagePaths:

    # ret, img =cam.read()
    img = cv2.imread(imagePath)
    # img = cv2.flip(img, -1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #cv2.imshow('camera', gray)
    #k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    #if k == 27:
    #    break 

    faces = faceCascade.detectMultiScale( 
        gray,
        # scaleFactor = 1.2,
        # minNeighbors = 5,
        # minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less then 100 ==> "0" is perfect match 
        if (confidence < 12 ):
            # id = names[id]
            confidence1 = "  {0}%".format(round(confidence))
            print("Confidence == " + str(confidence1) + "    ID == " + str(id) + "    Image Path == " + imagePath)
            
            count+=1
            accuracy.append(confidence)
            image_name.append(imagePath)
            
            target_img=cv2.imread(imagePath)
            plt.figure()
            plt.imshow(target_img)
            
            
            
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,0,0), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

        
        


# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")

    
print("Confidence values ")
x=[]

for i in range(len(accuracy)):
    x.append(i)

accuracy1=[]
print(accuracy)
print(image_name)
for i in accuracy:
    accuracy1.append(100-int(i))
    

plot_bar_x(x,accuracy1)


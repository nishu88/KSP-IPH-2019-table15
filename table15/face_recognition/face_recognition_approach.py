import pandas as pd
import cv2
from IPython.display import Image
from matplotlib import pyplot as plt
import face_recognition
import os
data = pd.read_csv("datasheet.csv") 
#print(data.head())

x=data["path"]

path_to_trainimages= "train_images/"
trainimages=os.listdir(path_to_trainimages)

path_to_testimages="test_images/"
arrest="cropped_arrest/"
death="cropped_death/"
wanted="cropped_wanted/"

train_arrest=os.listdir(path_to_testimages+arrest)
train_death=os.listdir(path_to_testimages+death)
train_wanted=os.listdir(path_to_testimages+wanted)

#print(trainimages[0:10],"\n",train_arrest[0:10],"\n",train_death[0:10],"\n",train_wanted[0:10])



image_emb_hash={}

folder_path="matched_pics/"
count=0

for i in trainimages:
    print("creating folder for ")
    print(i)
    
    try:
        os.mkdir(folder_path+i)
    except:
        pass
    var1=0
    
    
    face_image = face_recognition.load_image_file(path_to_trainimages+i)
    if len(face_recognition.face_encodings(face_image))!=0:
        face_encoding = face_recognition.face_encodings(face_image)[0]
    
    
    for j in train_arrest:
        to_match = face_recognition.load_image_file(path_to_testimages+arrest+j)
        if len(face_recognition.face_encodings(to_match))!=0:
            to_match_enc = face_recognition.face_encodings(to_match)[0]
            result = face_recognition.compare_faces([face_encoding], to_match_enc)
            
            if result[0]==True:
                print(result)
                img=cv2.imread(path_to_testimages+arrest+j)
                cv2.imwrite(folder_path+i+"/"+str(var1)+"image.jpg",img)
                var1+=1
                
        var1+=1
        print(var1,"-----------")
        #if var1==5:
        #   break
        
    var1=0
    for j in train_wanted:
        to_match = face_recognition.load_image_file(path_to_testimages+wanted+j)
        if len(face_recognition.face_encodings(to_match))!=0:
            to_match_enc = face_recognition.face_encodings(to_match)[0]
            result = face_recognition.compare_faces([face_encoding], to_match_enc)
            
            #img=cv2.imread(path_to_testimages+wanted+j)
            #cv2.imwrite(folder_path+i+"/"+str(var1)+"image.jpg",img)
            
            if result[0]==True:
                print(result)
                img=cv2.imread(path_to_testimages+wanted+j)
                cv2.imwrite(folder_path+i+"/"+str(var1)+"image.jpg",img)
                var1+=1
                
        var1+=1
        print(var1)
        #if var1==5:
        #   break
    
    count+=1
    if count==20:
        break
        
    
    



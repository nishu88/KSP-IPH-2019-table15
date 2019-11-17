import pandas as pd
import os

data=pd.read_csv("datasheet.csv")

#data.head()

l=os.listdir("train_dataset")
count = 1

for i in l:
    try:
        os.rename("train_dataset/"+i , "train_dataset/User."+str(count)+"."+str(count)+".jpg")
        #print(count)
        count+=1
    except:
        pass
    

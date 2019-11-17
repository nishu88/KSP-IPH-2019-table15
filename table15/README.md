# India-Police-Hackathon-2019


facial recognition for missing person.txt has the entire synopsis of the project <br/>

# HOW TO RUN <br/>
The manin.ipynb file has the entire code for training and testing
Every cell is commented to explain what each cell does </br>

The cells run  datacropping, facial feature extraction, training using cnn, and testing on the embeddings<br/>

## Folder descriptions

train_dataset_cropped - the training data images </br>
final_dataset_cropped - testing data images </br>

Vpree - Vpree approach for training and testing to create embeddings</br>
simple run the files present within the folder</br

face_eye_ears_mapping - holds a test image for te input to face_mappings.py file, which creates mappings for eyes nose ears as trains<br/>

face_recogntion - training using CNN approach <br/>

## File descriptions
data_rename.py - Run to rename image datasets to specific requirement <br/>
face_detection_and_crop - To detect faces and crops them and stores <br/>



Modules IMPLEMENTED :-

### Extracting face from data
<br />
 This crops the image to focus only on the facial features of a person
 
 ![image](https://user-images.githubusercontent.com/29069343/69004596-21530c80-093c-11ea-94d5-32a4cf78d06f.png)
 
 
 ### Face mapping outputs<br/>
 
 Using HOG extrating the features from the nose, ears and eyes
 ![image](https://github.com/nishu88/KSP-IPH-2019-table15/blob/master/table15/Outputs/face_features.JPG)
 
 
 
Using CNN to train and extract features and find the exact mapping the in test set<br/>
Used LBHP with the CNN model to extract the histogram values and the hamming distance between each image embedding is used to compare    the closeness of the image
 ![image](https://github.com/nishu88/KSP-IPH-2019-table15/blob/master/table15/Outputs/face_matching_hog.JPG)
 
 <br/>
 Outputs from VPtree method
 
 ![image](https://github.com/nishu88/KSP-IPH-2019-table15/blob/master/table15/Outputs/vptree.JPG)
 
 
 ### cctv monitor
<br />
 This actively monitors a online LIVE cctv link and makes a search database
  
 ![image](https://user-images.githubusercontent.com/29069343/69004616-75f68780-093c-11ea-8cb4-96d7173ec0e0.png)
  
  
  ### Social media mapper (2nd part of problem statement)
 <br />
  
With the help of social media search, we can easily search for people on social media platforms. Our mapper uses Facebook's existing APIs which takes the name and image of the missing person as an input. For using this API we must pass our facebook credentials as parameters to the API in order to fetch results. We get results in the form of a table embedded insisde an HTML file, using Django framework. Each row of the table contains the profile pic on facebook, name of the person and the profile link.
  
  ![result](https://user-images.githubusercontent.com/29069343/69004652-ffa65500-093c-11ea-81aa-e8b4b209e63b.png)
  
  
## Mobile Application based on Android And Flask
 <br />
In order to easily interface with the the facial detection, we created a mobile application on Android Platform, by which the user can upload the image to a server which will do the processing and fetch back the results. With the help of OKHTTP API which provides an easy framework for sending and receiving large objects over HTTP. The app asks the user to select the image of the missing person from the device. It then sends this to the server by asking the user the IPv4 Address and Port Number of the server. 

To make it easily to process, we are using a python based Flask Server running on a particular port number on the server. On the server side, it fetches the file that has been sent and saves it. After this, with the help of Local Binary Patterns Histogram (LBPH) algorithm implemented in OpenCV, the procecss calculates the confidence and fetches the ID. In case it is unable to fetch any ID, it returns as "unknown". After this computation is done, it fetches the result back to the Android client.

![image](https://user-images.githubusercontent.com/29069343/69004691-9115c700-093d-11ea-82ea-4efa4ca484bf.png)

![image](https://user-images.githubusercontent.com/29069343/69004696-abe83b80-093d-11ea-95ac-37f124514802.png)




 
 

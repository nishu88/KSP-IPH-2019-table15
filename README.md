# India-Police-Hackathon-2019

Modules IMPLEMENTED :-

### Extracting face from data
<br />
 this crops the image to focus only on the facial features of a person
 
 ![image](https://user-images.githubusercontent.com/29069343/69004596-21530c80-093c-11ea-94d5-32a4cf78d06f.png)
 
 
 ### face_eye_ears mapping
 <br />
  this considers only important parts of the face a highlights them
  
  ![face_features](https://user-images.githubusercontent.com/29069343/69004714-fb2e6c00-093d-11ea-8c4b-9c3651fcad68.JPG)
 
 
 ### face_recognition using police database and mapping MISSING with ARRESTED/WANTED
  <br />
   this maps missing and arrested with 70-80% accuracy
   
   ![face_matching_hog](https://user-images.githubusercontent.com/29069343/69004755-55c7c800-093e-11ea-8f3d-cb9173e328bb.JPG)
   
   ![vptree](https://user-images.githubusercontent.com/29069343/69004758-5ceed600-093e-11ea-81b5-53cac0a72452.JPG)
   
   ![webcam recognition](https://user-images.githubusercontent.com/29069343/69004760-637d4d80-093e-11ea-9349-ba8e8a81338e.png)
   
   
 
 
 ### cctv monitor
<br />
  this actively monitors a online LIVE cctv link and makes a search database
  
  ![image](https://user-images.githubusercontent.com/29069343/69004616-75f68780-093c-11ea-8cb4-96d7173ec0e0.png)
  
  
  ### Social media mapper (2nd part of problem statement)
 <br />
  this searches for a person on social media by considering his preprocessed image and his name,age,place obtained from the police records
  
  ![result](https://user-images.githubusercontent.com/29069343/69004652-ffa65500-093c-11ea-81aa-e8b4b209e63b.png)
  
  
## Mobile Application based on Android And Flask
 <br />
In order to easily interface with the the facial detection, we created a mobile application on Android Platform, by which the user can upload the image to a server which will do the processing and fetch back the results. With the help of OKHTTP API which provides an easy framework for sending and receiving large objects over HTTP. The app asks the user to select the image of the missing person from the device. It then sends this to the server by asking the user the IPv4 Address and Port Number of the server. 

To make it easily to process, we are using a python based Flask Server running on a particular port number on the server. On the server side, it fetches the file that has been sent and saves it. After this, with the help of Local Binary Patterns Histogram (LBPH) algorithm implemented in OpenCV, the procecss calculates the confidence and fetches the ID. In case it is unable to fetch any ID, it returns as "unknown". After this computation is done, it fetches the result back to the Android client.

![image](https://user-images.githubusercontent.com/29069343/69004691-9115c700-093d-11ea-82ea-4efa4ca484bf.png)

![image](https://user-images.githubusercontent.com/29069343/69004696-abe83b80-093d-11ea-95ac-37f124514802.png)



 
 

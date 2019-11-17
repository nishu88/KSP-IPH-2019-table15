# India-Police-Hackathon-2019

Modules IMPLEMENTED :-

### Extracting face from data
<br />
 this crops the image to focus only on the facial features of a person
 
 ![image](https://user-images.githubusercontent.com/29069343/69004596-21530c80-093c-11ea-94d5-32a4cf78d06f.png)
 
 
 ### cctv monitor
<br />
  this actively monitors a online LIVE cctv link and makes a search database
  
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



## Running 
<br/>
Open main.ipynb file and run,

The cells run as follows- 
1st Cell - datacropping with facial recognition
2nd Cell - Used to perform facial face detection and feature extracton
3rd Cell - runs the training model, to create embeddings for the input images
4th Cell - Used for predicting closest match among the test pictures and plot accuracy curve




 
 

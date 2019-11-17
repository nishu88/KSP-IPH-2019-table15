import flask
import werkzeug
import time
import cv2
import numpy as np
import os 
from flask import send_file
from flask import jsonify

recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

font=cv2.FONT_HERSHEY_SIMPLEX


id=''
confidence=''

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def handle_request():
    files_ids = list(flask.request.files)
    print("\nNumber of Received Images : ", len(files_ids))
    
    for file_id in files_ids:
        print("\nSaving Image ", str('0'), "/", len(files_ids))
        imagefile = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        print("Image Filename : " + imagefile.filename)
        imagefile.save(filename)
        img=cv2.imread(filename)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id, confidence=recognizer.predict(gray[y:y+h,x:x+w])
            if confidence<100 and confidence<30:
                confidence=' {0}%'.format(round(100-confidence))
                print('Confidence =='+str(confidence)+' id=='+str(id))
            else:
                id='unknown'
                confidence=' {0}%'.format(round(100-confidence))
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,0,0), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
            
        cv2.imwrite(filename,img)
        print('written')
        
    print("\n")
    return "Image(s) Uploaded Successfully. Come Back Soon."

@app.route('/get_image')
def get_image():
    return send_file('Android_Flask_0.jpg', mimetype='image/gif')

@app.route('/get_params')
def get_params():
    return jsonify(id=id, confidence=confidence)



app.run(host="0.0.0.0", port=5000, debug=True)

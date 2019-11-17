import cv2
import sys
import os
#import face_recognition



class FaceCropper(object):
    CASCADE_PATH = "Resource/haarcascade_frontalface_default.xml"

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(self.CASCADE_PATH)

    def generate(self, image_path, iii,show_result):
        img = cv2.imread(image_path)
        if (img is None):
            print("Can't open image file")
            return 0

        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(img, 1.1, 3, minSize=(100, 100))
        if (faces is None):
            print('Failed to detect face')
            return 0

        """if (show_result):
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            cv2.imshow('img', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        """
        
        facecnt = len(faces)
        print("Detected faces: %d" % facecnt)
        i = 0
        height, width = img.shape[:2]

        for (x, y, w, h) in faces:
            r = max(w, h) / 2
            centerx = x + w / 2
            centery = y + h / 2
            nx = int(centerx - r)
            ny = int(centery - r)
            nr = int(r * 2)

            faceimg = img[ny:ny+nr, nx:nx+nr]
            lastimg = cv2.resize(faceimg, (100, 100))
            i += 1
            print("g"+str(i)+"g"+ iii)
            cv2.imwrite("g"+str(i)+"g"+ iii , lastimg)


if __name__ == '__main__':
    

    detecter = FaceCropper()
    for i in os.listdir(r'C:\Users\nisha\Desktop\KSP Hack\b_images'):

        print(i)
        img = cv2.imread(r'C:\Users\nisha\Desktop\KSP Hack\b_images/'+i,0)       
        detecter.generate(r'C:\Users\nisha\Desktop\KSP Hack\b_images/'+i,i, True)

##
##    image_to_be_matched = cv2.imread("rajat.jpg")
##
##    images = cv2.imread("image1.jpg")
##
##    if len(face_recognition.face_encodings(image_to_be_matched))!=0:
##        image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]
##    else:
##        print("face not detected")
##
##            
##   
##    if len(face_recognition.face_encodings(images))!=0:
##        current_image_encoded = face_recognition.face_encodings(images)[0]
##    result = face_recognition.compare_faces([image_to_be_matched_encoded], current_image_encoded)
##    print(result[0])

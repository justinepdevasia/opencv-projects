import cv2
import numpy as np
import os
import funtionfordet
j=1
p=0
os.system("python facedetectionmodule.py")
print("hello")	

#after the execution of above code face is detected 
#a photo is taken and stored inside the test-data folder
#now we have to implement the face detection function
#function to detect face

while(True):
	   if os.path.exists('test-data/'+str(j)+'.jpg'):
	       j=j+1
	   else:
	       break

p=j-1

print("Preparing data...")
faces, labels = funtionfordet.prepare_training_data("training-data")
print("Data prepared")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))

#print total faces and labels
print("Total faces: ", len(faces))
print("Total labels: ", len(labels))

#here we have to read the current photo from the
#folder and fed it to trainning data
img = cv2.imread("test-data/"+str(p)+".jpg")
face, rect = funtionfordet.detect_face(img)

label, confidence = face_recognizer.predict(face)

print(label)
print(confidence)
print(p)

#the label returns an integer value that is related with the 
#folder name after detection ie; s1,s2,s3 etc...
#1 indicates person in in first folderlike that.

#condition
if label>0:
	file=open("user-info/"+str(label)+".txt","r")
	a=file.read()
	print(str(a))
	os.system("espeak "+str(a))
	os.system("espeak hello---"+str(a))
	os.system("espeak thankyou--for-being--my--friend")


else:
	os.system("python filewrite.py")




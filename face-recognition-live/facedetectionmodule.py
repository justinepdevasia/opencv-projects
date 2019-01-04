import cv2
import numpy as np
import os

#here we put some variables for our use
facenum=0




cap=cv2.VideoCapture(0)
while(True):

    #this code is for detecting faces in the video
	ret,frame=cap.read()
	cv2.imshow('frame',frame)
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
	faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
	print('Faces found:',len(faces))
    	if len(faces)==1:
     	 facenum=facenum+1
    	if facenum==10:
    	#here we try to capture a photo
    	 cap.release()
     	 os.system('python testphotocapture.py')
     	 break
    	if cv2.waitKey(1) & 0xFF==ord('q'):
	     	  break
	     	  
cap.release()
cv2.destroyAllWindows()
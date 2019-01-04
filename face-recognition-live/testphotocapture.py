import cv2
import numpy as np
import os

j=1
k=1
currentFrame=1
# Playing video from camera:
cam = cv2.VideoCapture(0)


while(True):
	   if os.path.exists('test-data/'+str(j)+'.jpg'):
	       j=j+1
	   else:
	       break
#taking photo

while(True):

	 if(k==1):

	             
	   os.system("espeak "+"capturing----photo")
   	   # Capture frame-by-frame
  	   ret, frame = cam.read()
	
   	   # Saves image of the current frame in jpg file
  	   name = './test-data/'+ str(j) + '.jpg'
   	   print ('Creating...' + name)
   	   cv2.imwrite(name, frame)
	   cam.release()
   	   # To stop duplicate images
   	   #k=k+1
	   break
	   
	 else:
	   break
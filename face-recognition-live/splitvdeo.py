
import cv2
import numpy as np
import os
i=1
# Playing video from camera:
cap = cv2.VideoCapture(0)

while(True):
	try:
    		if not os.path.exists('training-data/s'+str(i)):
        		os.makedirs('training-data/s'+str(i))
			break

		i=i+1

	except OSError:
   	     print ('Error: Creating directory of data')

currentFrame = 1
while(currentFrame<=10):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './training-data/s'+str(i)+'/'+ str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1


	


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

#####################################
##### Developed by Marwen Doukh #####
#####################################


#import openCV library
import cv2
import sys

#import a trained classifier
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


image = cv2.imread(sys.argv[1])

#detect the face using the classifier
faces = faceCascade.detectMultiScale(
        #the image to use
        image,
        scaleFactor=1.1,
        minNeighbors=5,
        #specify the minimal object size , if it is smaller than 20*20 it will not be retained
        minSize=(20, 20)
    )

#draw a red rectangle around the object detected
for (x, y, w, h) in faces:
   cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# show the final image
cv2.imshow("face", image)
#keep the window , do not close until the user press a button
cv2.waitKey(0)

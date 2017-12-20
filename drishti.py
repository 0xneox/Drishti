import cv2
import sys
import glob
import imghdr
from wand.image import Image
 
# Create the haar cascade
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
 
 # Get user supplied images
files_grabbed = [glob.glob(e) for e in ['images/*.jpg', 'images/*.png']]
files=[]
for filetype in files_grabbed:
    for image in filetype:
        files.append(image)
 
for img in files:
    print(img)
    if imghdr.what(img) == None: # Some images from google can be broken, so we checking it there
        print(img+" bad image")
        continue # If image is broken we continue our loop ignoring it
    else:
        orIm = Image(filename=img)
 
 
    # Read the image
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # opencv need black and white picture
 
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray, # image for detection
        scaleFactor=1.1, # you can adjust this params to increase detection quality
        minNeighbors=5,  # and
        minSize=(30, 30) # this too
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )
 
 
    i=1 # counnter
 
    # Edit image and save it to data folder
    for (x, y, w, h) in faces:
        imgg=Image(filename=img)
        orIm.crop(x,y,x+w,y+h) # croping out face
        orIm.resize(256,256) # face image resizing
        orIm.save(filename=img.replace('images/','exit_data/'+str(i))) # save it to data folder
        orIm = Image(imgg) # if picture has more than 1 face reload it
        i+=1

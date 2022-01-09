import face_recognition
import os
import time
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

if __name__=='__main__':
    deskLEDsPin = 24

    #load known pictures
    #make array of knowns
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(deskLEDsPin, GPIO.OUT)
    camera = PiCamera()
    path = r"/home/pi/Desktop/speechBot/Pictures/Archive"
    picPath = "Pictures/Archive/"
    knownDirectory = os.listdir( path )
    encodedArray = []
    faceRecTries = 0
    maxFaceRexTries = 10

    for file in knownDirectory:
        print(picPath+file)
        known_image = face_recognition.load_image_file(picPath+file)
        known_image_encoding = face_recognition.face_encodings(known_image)[0]
        encodedArray.append(known_image_encoding)


    unkFileName = "tmp/picture.jpg"

    while True:
        #TODO out of resources, change file name
        foundFace = False
        os.system("sudo rm "+unkFileName)
        
        
        camera.start_preview()
        sleep(0.1)
        camera.capture(unkFileName)
        camera.stop_preview()

        unknown_image = face_recognition.load_image_file(unkFileName)
        unknown_encoding = face_recognition.face_encodings(unknown_image)

        if len(unknown_encoding) > 0:
            unknown_encoding = unknown_encoding[0]

            results = face_recognition.compare_faces(encodedArray, unknown_encoding)
            
            for found_face in results:
                if found_face:
                    foundFace = True
                    break
        
        if foundFace is False:
            faceRecTries += 1
        
        if foundFace:
            GPIO.output(deskLEDsPin, False) #turned on
            faceRecTries = 0
            #time.sleep(300)  #can set delay or raise number of times can fail
        elif faceRecTries > maxFaceRexTries:
            GPIO.output(deskLEDsPin, True) #turned off
            faceRecTries = 0

if __name__=="__exit__": 
        print('exit method called')
        GPIO.cleanup()  


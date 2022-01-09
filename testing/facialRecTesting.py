import face_recognition
import os
from picamera import PiCamera
from time import sleep

#load known pictures
#make array of knowns
camera = PiCamera()
path = r"/home/pi/Desktop/Bot/speechBot/Pictures/Archive"
picPath = "Pictures/Archive/"
knownDirectory = os.listdir( path )
encodedArray = []

for file in knownDirectory:
    print(picPath+file)
    known_image = face_recognition.load_image_file(picPath+file)
    known_image_encoding = face_recognition.face_encodings(known_image)[0]
    encodedArray.append(known_image_encoding)


unkFileName = "tmp/picture.jpg"

while True:
    #TODO out of resources, change file name
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
                print("I see you!")
                break

        print(results)

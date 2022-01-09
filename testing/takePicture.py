#!/usr/bin/env python

from picamera import PiCamera
from time import sleep

imagePath = 'Pictures/Archive/John_10.jpg'
#imagePath = 'tmp/picture.jpg'

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture(imagePath)
camera.stop_preview()

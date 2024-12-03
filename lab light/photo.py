from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (1280, 720)
camera.start_preview()
time.sleep(2)
camera.capture('photo_white.png')
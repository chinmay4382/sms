from picamera import PiCamera
import time
camera=PiCamera()
camera.resolution=(512,512)
camera.start_preview()
time.sleep(2)
camera.capture("guru1.jpg")
camera.stop_preview()
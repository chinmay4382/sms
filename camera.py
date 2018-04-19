import RPi.GPIO as IO
from picamera import PiCamera
import time
camera=PiCamera()
camera.resolution=(512,512)
IO.setmode(IO.BCM)
IO.setup(14,IO.IN) #GPIO 14 -> IR sensor as input for bio degradable 
while True:
	if (IO.input(14)!=False): #object is near
			time.sleep(2)
			if (IO.input(14)!=False):
				camera.start_preview()
				time.sleep(2)
				camera.capture("image.jpg")
				camera.stop_preview()
		
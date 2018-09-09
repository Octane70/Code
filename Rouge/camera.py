from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 270 

camera.start_preview()
sleep(3)
camera.capture('/home/pi/rouge/captures/image.jpg')
camera.stop_preview()



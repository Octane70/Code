import RPi.GPIO as gpio
import time

#INITIAL SETUP
gpio.setmode(gpio.BCM)
enable_pin=17
gpio.setup(enable_pin, gpio.OUT)
gpio.output(enable_pin, gpio.LOW)

left_forward=22
left_reverse=23
right_forward=24
right_reverse=25

gpio.setup(left_forward, gpio.OUT)
gpio.setup(left_reverse, gpio.OUT)
gpio.setup(right_forward, gpio.OUT)
gpio.setup(right_reverse, gpio.OUT)





def reset_all():
	#set all GPIOs to low
	gpio.output(left_forward, gpio.LOW)
	gpio.output(left_reverse,gpio.LOW)
	gpio.output(right_forward, gpio.LOW)
	gpio.output(right_reverse,gpio.LOW)

def go(direction, duration,speed):
	reset_all()
	pwm=gpio.PWM(enable_pin, 80)
	pwm.start(speed)
	#pwm.ChangeDutyCycle(speed)
	if direction=="forward":
		gpio.output(right_forward, gpio.HIGH)
		gpio.output(left_forward, gpio.HIGH)
	elif direction=="reverse":
		gpio.output(right_reverse,gpio.HIGH)
		gpio.output(left_reverse,gpio.HIGH)
	elif direction=="left":
		gpio.output(left_reverse, gpio.HIGH)
		gpio.output(right_forward, gpio.HIGH)
	elif direction=="right":
		gpio.output(right_reverse, gpio.HIGH)
		gpio.output(left_forward, gpio.HIGH)
		
	time.sleep(duration)
	pwm.stop()
	
def take_photo():
	pic=picam.takePhotoWithDetails(640,480,75)
	filename="image" +time.strftime("%Y%m%d-%H%M%S")+".jpg"
	pic.save(filename)


take_photo()
go("forward",2,100)
take_photo()
go("reverse",2,80)
take_photo()
go("left",2,50)
take_photo()
go("right",1,100)
take_photo()


gpio.cleanup()

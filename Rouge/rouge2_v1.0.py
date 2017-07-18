from bluedot import BlueDot
import RPi.GPIO as GPIO
from signal import pause

print ("Rouge 2 is online")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT) # purple // 1in
GPIO.setup(18, GPIO.OUT) # blue // 2in
#GPIO.setup(32, GPIO.OUT) # white // 1pwm
#GPIO.setup(12, GPIO.OUT) # grey // 2pwm
GPIO.setup(15, GPIO.OUT) # green // 3in
GPIO.setup(11, GPIO.OUT) # yellow // 4in
GPIO.setwarnings(False)

#rh = GPIO.PWM(12,120) #white // 1pwm
#rh.start(10) #start right motor at 50% duty cycle
# rh.ChangeDutyCycle(0)

#lh = GPIO.PWM(32,120) #grey // 2pwm
#lh.start(10) #start left motor at 50% duty cycle
# lh.ChangeDutyCycle(0)

#set all Motors to False
GPIO.output(16, False)
GPIO.output(18, False)
GPIO.output(15, False)
GPIO.output(11, False)

def dpad(pos):
    if pos.top:
        GPIO.output(16, False) #Left Motor // 1ina
        GPIO.output(18, True)  #Left Motor // 1inb
        GPIO.output(11, True)  #Right Motor // 2ina
        GPIO.output(15, False) #Right Motor // 2inb
        print("forward")
    elif pos.bottom:
        GPIO.output(16, True)  #Left Motor // 1ina
        GPIO.output(18, False) #Left Motor // 1inb
        GPIO.output(11, False) #Right Motor // 2ina
        GPIO.output(15, True)  #Right Motor // 2inb
        print("reverse")
    elif pos.left:
        GPIO.output(16, False)  #Left Motor // 1ina
        GPIO.output(18, True) #Left Motor // 1inb
        GPIO.output(11, False)  #Right Motor // 2ina
        GPIO.output(15, True) #Right Motor // 2inb
        print("left")
    elif pos.right:
        GPIO.output(16, True) #Left Motor // 1ina
        GPIO.output(18, False)  #Left Motor // 1inb
        GPIO.output(11, True) #Right Motor // 2ina
        GPIO.output(15, False)  #Right Motor // 2inb
        print("right")
    elif pos.middle:
        #Turn off the motors
        #GPIO.output(12, False)
        #GPIO.output(32, False)
        GPIO.output(16, False)
        GPIO.output(18, False)
        GPIO.output(15, False)
        GPIO.output(11, False)
        #GPIO.cleanup()
        print("all stop")

bd = BlueDot()
bd.when_pressed = dpad

pause()

GPIO.cleanup()
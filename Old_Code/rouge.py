import RPi.GPIO as gpio
import time

#Set GPIO mode
gpio.setmode(gpio.BCM)
#Set output pins
PWM1=17
PWM2=23
IN1a=22
IN1b=27
IN2a=25
IN2b=24

gpio.setup(PWM1, gpio.OUT)
gpio.setup(PWM2, gpio.OUT)
gpio.setup(IN1a, gpio.OUT)
gpio.setup(IN1b, gpio.OUT)
gpio.setup(IN2a, gpio.OUT)
gpio.setup(IN2b, gpio.OUT)
#Set enable pins
gpio.output(PWM1, True)
gpio.output(PWM2, True)

while True:
    gpio.output(IN1a, True)
    gpio.output(IN1b, False)
    #gpio.output(25, True)
    #gpio.output(24, False)
    time.sleep(0)
    #gpio.output(IN1a, False)
    #gpio.output(IN1b, True)
    #gpio.output(25, False)
    #gpio.output(24, True)
    #time.sleep(1)
    #gpio.output(IN1a, False)
    #gpio.output(25, False)


gpio.cleanup()

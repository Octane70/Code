import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)

gpio.output(18, True)
n=raw_input ("enter no of seconds")

while True:
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(float (n))
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(float (n))
    gpio.output(18, False)
    
gpio.cleanup()

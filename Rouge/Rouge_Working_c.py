    #!/usr/bin/env python

import pygame
import RPi.GPIO as gpio
import serial
import time
import sys
import tty

# Initialize port
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)

# Initialise the pygame library
pygame.init()

# Connect to the first JoyStick
j = pygame.joystick.Joystick(0)
j.init()

print 'Initialized Joystick : %s' % j.get_name()

gpio.setmode(gpio.BOARD)
gpio.setup(16, gpio.OUT) # brown // 1ina
gpio.setup(18, gpio.OUT) # Yellow // 1inb
gpio.setup(32, gpio.OUT) # blue // 1pwm
gpio.setup(12, gpio.OUT) # purple // 2pwm
gpio.setup(15, gpio.OUT) # green // 2inb
gpio.setup(11, gpio.OUT) # orange // 2ina
gpio.setwarnings(False)
    
# gpio.output(12, True) #purple // 1pwm
#gpio.output(32, True) #blue // 2pwm
      
rh = gpio.PWM(12,120) #purple // 1pwm
rh.start(10) #start right motor at 50% duty cycle
# rh.ChangeDutyCycle(0)

lh = gpio.PWM(32,120) #blue // 2pwm
lh.start(10) #start left motor at 50% duty cycle
# lh.ChangeDutyCycle(0)

#set all Motors to False
gpio.output(16, False)
gpio.output(18, False)
gpio.output(15, False)
gpio.output(11, False)

# Only start the motors when the inputs go above the following threshold
threshold = 0.60


LeftTrack = 0
RightTrack = 0
Servo1Up = 0
Servo1Dwn = 0
Servo2Rht = 0
Servo2Lft = 0
Button_O = 0

# Min, Mid, Max PWM
Min = 500
Mid = 1500
Max = 2500

# Add Variables
var = Mid
#servo_up > Max, var = Max
#servo_down < Min, var = Min
servo_up = var+50
servo_down = var-50
servo_right = var+50
servo_left = var-50

# Key Mappings
RH_JOYSTICK_UP_DWN = 3  # Right Joystick up to down values -1.0 to 0.99
LH_JOYSTICK_UP_DWN = 1  # Left Joystick up to down values -1.0 to 0.99
PS3_AXIS_DPAD_UP = 8
PS3_AXIS_DPAD_RIGHT = 9
PS3_AXIS_DPAD_DOWN = 10
PS3_AXIS_DPAD_LEFT = 11
PS3_AXIS_L2 = 12
PS3_AXIS_R2 = 13
PS3_AXIS_L1 = 14
PS3_AXIS_R1 = 15
PS3_AXIS_O = 17
PS3_AXIS_X = 18

# Define Left Motor Forward
def left_forward():
    gpio.output(16, True) #Left Motor // 1ina 
    gpio.output(18, False)  #Left Motor // 1inb
    
# Define Right Motor Forward
def right_forward():
    gpio.output(11, False)  #Right Motor // 2ina  
    gpio.output(15, True) #Right Motor // 2inb

# Define Left Motor Backward   
def left_backward():
    gpio.output(16, False)  #Left Motor // 1ina  
    gpio.output(18, True) #Left Motor // 1inb
    
# Define Roght Motor Backward
def right_backward():   
    gpio.output(11, True) #Right Motor // 2ina   
    gpio.output(15, False)  #Right Motor // 2inb
    	   	           
def forward():
    gpio.output(16, True) #Left Motor // 1ina 
    gpio.output(18, False)  #Left Motor // 1inb
    gpio.output(11, False)  #Right Motor // 2ina  
    gpio.output(15, True) #Right Motor // 2inb
    
def backward():
    gpio.output(16, False)  #Left Motor // 1ina  
    gpio.output(18, True) #Left Motor // 1inb 
    gpio.output(11, True) #Right Motor // 2ina   
    gpio.output(15, False)  #Right Motor // 2inb

def turn_left():
    gpio.output(16, False) #Left Motor // 1ina 
    gpio.output(18, True)  #Left Motor // 1inb 
    gpio.output(11, False) #Right Motor // 2ina 
    gpio.output(15, True)  #Right Motor // 2inb     

def turn_right():
    gpio.output(16, True)  #Left Motor // 1ina 
    gpio.output(18, False) #Left Motor // 1inb  
    gpio.output(11, True)  #Right Motor // 2ina
    gpio.output(15, False) #Right Motor //  2inb 

def pivot_left():
    gpio.output(16, False) #Left Motor // 1ina	 
    gpio.output(18, False) #Left Motor // 1inb
    gpio.output(11, False) #Right Motor // 2ina 
    gpio.output(15, True)  #Right Motor // 2inb

def pivot_right():
    gpio.output(16, True)  #Left Motor // 1ina 
    gpio.output(18, False) #Left Motor // 1inb  
    gpio.output(11, False) #Right Motor // 2ina
    gpio.output(15, False) #Right Motor // 2inb
    
def all_stop():
    gpio.output(16, False) #Left Motor // 1ina 
    gpio.output(18, False) #Left Motor // 1inb  
    gpio.output(11, False) #Right Motor // 2ina
    gpio.output(15, False) #Right Motor // 2inb    
 
def servo1_up():
    port.write("#15P%dT100\r\n" % servo_up)
        
def servo1_down():
    port.write("#15P%dT100\r\n" % servo_down)
    
def servo2_right():
    port.write("#16P%dT100\r\n" % servo_right)
    
def servo2_left():
    port.write("#16P%dT100\r\n" % servo_left)
    
def servos_return():
	port.write("#15P1500T100\r\n")
	port.write("#16P1500T100\r\n")     
          
try:
	# Turn on the motors
    gpio.output(12, True) #purple // 1pwm
    gpio.output(32, True) #blue // 2pwm
    
    while True:
		 
		# Check for any queued events and then process each one
        events = pygame.event.get()
        for event in events:
          UpdateMotors = 0

          # Check if one of the joysticks has moved
          if event.type == pygame.JOYAXISMOTION:
            if event.axis == RH_JOYSTICK_UP_DWN:
              RightTrack = event.value
              UpdateMotors = 1
            elif event.axis == LH_JOYSTICK_UP_DWN:
              LeftTrack = event.value
              UpdateMotors = 1
            elif event.axis == PS3_AXIS_R2:
              Servo1Up = event.value
              UpdateMotors = 1
            elif event.axis == PS3_AXIS_L2:
              Servo1Dwn = event.value
              UpdateMotors = 1
            elif event.axis == PS3_AXIS_R1:
              Servo2Rht = event.value
              UpdateMotors = 1
            elif event.axis == PS3_AXIS_L1:
              Servo2Lft = event.value
              UpdateMotors = 1
            elif event.axis == PS3_AXIS_O:
               Button_O = event.value
               UpdateMotors = 1              

            # Check if we need to update what the motors are doing
            if UpdateMotors:

	          # Right Track Forward and Reverse Values
	          if (RightTrack > threshold):
	              print ("Right Track Forward")
	              right_forward()	              
	              rh.ChangeDutyCycle(25)

	          elif (RightTrack < -threshold):
	               print ("Right Track Backward")
	               right_backward()
	               rh.ChangeDutyCycle(25)

	          # Left Track Forward and Reverse Values
	          elif (LeftTrack > threshold):
	               print ("Left Track Forward")
	               left_forward()	              
	               lh.ChangeDutyCycle(25)

	          elif (LeftTrack < -threshold):
	               print ("Left Track Backward")
	               left_backward()
	               lh.ChangeDutyCycle(25)
	               
	          # Camera Up/Down & Right/Left Values      	               
	          elif (Servo1Up):
	               print ("Camera Up")
	               servo1_up()
	               time.sleep (0.1)
	               
	          elif (Servo1Dwn):
	               print ("Camera Down")
	               servo1_down()
	               time.sleep (0.1)

	          elif (Servo2Rht):
	               print ("Camera Right")
	               servo2_right()	               
	               time.sleep (0.1)
	               
	          elif (Servo2Lft):
	               print ("Camera Left")
	               servo2_left()	               
	               time.sleep (0.1)
	               
	          elif (Button_O):
	               print ("Camera Return")
	               servos_return()	               
	               time.sleep (0.1)
	               	               	               	               	                    
	          else:
				   all_stop()
				   lh.stop     
				   rh.stop
				   
	               

	
	#if(char == "x"):
	    #print("PROGRAM ENDED")
	    #break
	    #lh.ChangeDutyCycle(0)
	    #rh.ChanegDutyCycle(0)
	    
   	 

except KeyboardInterrupt:
    # Turn off the motors
    gpio.output(12, False) #purple // 1pwm
    gpio.output(32, False) #blue // 2pwm
    j.quit()#!/usr/bin/env python

gpio.cleanup()

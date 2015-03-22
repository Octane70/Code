#!/usr/bin/env python
#http://learnpythonthehardway.org/book/ex5.html

import pygame
import RPi.GPIO as gpio
import serial
import time
import sys
#import tty

# Initialize port
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)

# Initialise the pygame library
pygame.init()

# Connect to the first JoyStick
j = pygame.joystick.Joystick(0)
j.init()

print 'Initialized Joystick : %s' % j.get_name()


# Add Min, Mid & Max
servoMin = 700
servoMid = 1500
servoMax = 2300

# Add servo increments
servoTilt = 1500
servoPan = 1500
servostepTilt = 5
servostepPan = 5

# Key Mappings
RH_JOYSTICK_UP_DWN = 3  # Right Joystick up to down values -1.0 to 0.99
RH_JOYSTICK_LFT_RHT = 2 # Right Joystick left to right values -1.0 to 0.99
LH_JOYSTICK_UP_DWN = 1  # Left Joystick up to down values -1.0 to 0.99
LH_JOYSTICK_LFT_RHT = 0 # Left Joystick left to right values -1.0 to 0.99   
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
#PS3_AXIS_TRIANGLE = 12
#PS3_AXIS_SQUARE = 12

   
 
def servo1_left():
  global servoTilt
  servoTilt += servostepTilt
  if servoTilt > servoMax:
    servoTilt = servoMax
  port.write("#1P%dT100\r\n" % servoTilt)
    
def servo1_right():
  global servoTilt
  servoTilt -= servostepTilt
  if servoTilt < servoMin:
    servoTilt = servoMin
  port.write("#1P%dT100\r\n" % servoTilt)
    
def servo2_up():
  global servoPan
  servoPan += servostepPan
  if servoPan > servoMax:
    servoPan = servoMax
  port.write("#2P%dT100\r\n" % servoPan)
    
def servo2_down():
  global servoPan
  servoPan -= servostepPan
  if servoPan < servoMin:
    servoPan = servoMin
  port.write("#2P%dT100\r\n" % servoPan)

def servo3_up():
  global servoPan
  servoPan += servostepPan
  if servoPan > servoMax:
    servoPan = servoMax
  port.write("#3P%dT100\r\n" % servoPan)
    
def servo3_down():
  global servoPan
  servoPan -= servostepPan
  if servoPan < servoMin:
    servoPan = servoMin
  port.write("#3P%dT100\r\n" % servoPan)

def servo4_up():
  global servoPan
  servoPan += servostepPan
  if servoPan > servoMax:
    servoPan = servoMax
  port.write("#4P%dT100\r\n" % servoPan)
    
def servo4_down():
  global servoPan
  servoPan -= servostepPan
  if servoPan < servoMin:
    servoPan = servoMin
  port.write("#4P%dT100\r\n" % servoPan)

def servo5_left():
  global servoPan
  servoPan += servostepPan
  if servoPan > servoMax:
    servoPan = servoMax
  port.write("#5P%dT100\r\n" % servoPan)
    
def servo5_right():
  global servoPan
  servoPan -= servostepPan
  if servoPan < servoMin:
    servoPan = servoMin
  port.write("#5P%dT100\r\n" % servoPan)
  
def servoclaw_open():
  global servoPan
  servoPan += servostepPan
  if servoPan > servoMax:
    servoPan = servoMax
  port.write("#6P%dT100\r\n" % servoPan)
    
def servoclaw_close():
  global servoPan
  servoPan -= servostepPan
  if servoPan < servoMin:
    servoPan = servoMin
  port.write("#6P%dT100\r\n" % servoPan)
  
def servos_home():
  servoTilt = servoMid
  servoPan = servoMid
  port.write("#13P%dT100\r\n" % servoTilt)
  port.write("#16P%dT100\r\n" % servoPan)     

# Only start the motors when the inputs go above the following threshold
threshold = 0.60

Servo1_Lft_Rht = 0
Servo2_Up_Dwn = 0
Servo3_Up_Dwn = 0
Servo4_Up_Dwn = 0
Servo5_Lft = 0
Servo5_Rht = 0
ServoClawOpen = 0
ServoClawClosed = 0
Button_O = 0

try:

    
    while True:
     
    # Check for any queued events and then process each one
        events = pygame.event.get()
        for event in events:
          UpdateMotors = 0

          # Check if one of the joysticks has moved
          if event.type == pygame.JOYAXISMOTION:
            if event.axis == LH_JOYSTICK_LFT_RHT:
              Servo1_Lft_Rht = event.value
              UpdateMotors = 1
            elif event.axis == LH_JOYSTICK_UP_DWN:
              Servo2_Up_Dwn = event.value
              UpdateMotors = 1
            elif event.axis == RH_JOYSTICK_UP_DWN:
              Servo3_Up_Dwn = event.value
              UpdateMotors = 1
            elif event.axis == RH_JOYSTICK_LFT_RHT:
              Servo4_Up_Dwn = event.value
              UpdateMotors = 1
            elif event.axis == PS3_AXIS_L1:
              Servo5_Lft = event.value
              UpdateMotors = 1
            elif event.axis == PS3_AXIS_R1:
              Servo5_Rht = event.value
              UpdateMotors = 1
            elif event.axis == PS3_AXIS_L2:
              ServoClawOpen = event.value
              UpdateMotors = 1
            elif event.axis == PS3_AXIS_R2:
              ServoClawClosed = event.value
              UpdateMotors = 1              
            elif event.axis == PS3_AXIS_O:
               Button_O = event.value
               UpdateMotors = 1              
            elif event.axis == PS3_AXIS_X:
               Button_X= event.value
               UpdateMotors = 1
               
            # Check if we need to update what the motors are doing
            if UpdateMotors:
                 
            # Servo Up/Down & Right/Left Values                       
              if (Servo1_Lft_Rht < -threshold):
                 print ("Servo1 Left")
                 servo1_left()
                 time.sleep (0.01)
                 
              elif (Servo1_Lft_Rht > threshold):
                 print ("Servo1 Right")
                 servo1_right()
                 time.sleep (0.01)

              if (Servo2_Up_Dwn < -threshold):
                 print ("Servo2 Up")
                 servo2_up()                
                 time.sleep (0.01)
                 
              elif (Servo2_Up_Dwn > threshold):
                 print ("Servo2 Down")
                 servo2_down()                 
                 time.sleep (0.01)

              if (Servo3_Up_Dwn < -threshold):
                 print ("Servo3 Up")
                 servo3_up()                
                 time.sleep (0.01)
                 
              elif (Servo3_Up_Dwn > threshold):
                 print ("Servo3 Down")
                 servo3_down()                 
                 time.sleep (0.01)
                 
              if (Servo4_Up_Dwn > threshold):
                 print ("Servo4 Up")
                 servo4_up()                
                 time.sleep (0.01)
                 
              elif (Servo4_Up_Dwn < -threshold):
                 print ("Servo4 Down")
                 servo4_down()                 
                 time.sleep (0.01)
                 
              if (Servo5_Lft):
                 print ("Servo5 Left")
                 servo5_left()                
                 time.sleep (0.01)
                 
              elif (Servo5_Rht):
                 print ("Servo5 Right")
                 servo5_right()                 
                 time.sleep (0.01)
                 
              if (ServoClawOpen):
                 print ("Servo1 Opening")
                 servoclaw_open()                
                 time.sleep (0.01)
                 
              elif (ServoClawClosed):
                 print ("Servo Closing")
                 servoclaw_close()                 
                 time.sleep (0.01)                 
                 
              elif (Button_O):
                 print ("Camera Return")
                 servos_return()                 
                 time.sleep (0.01)
                                                                                      
                                
    #time.sleep (0.01)

      
     

except KeyboardInterrupt:
    j.quit()#!/usr/bin/env python

gpio.cleanup()

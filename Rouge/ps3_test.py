#!/usr/bin/env python
#http://www.mybigideas.co.uk/RPi/BigTrak/softwarepython.php
#http://www.raspians.com/Knowledgebase/ps3-dualshock-controller-install-on-the-raspberry-pi/

import pygame
import time
import RPi.GPIO as GPIO

# Initialise the pygame library
pygame.init()

# Connect to the first JoyStick
j = pygame.joystick.Joystick(0)
j.init()

print 'Initialized Joystick : %s' % j.get_name()

# Setup the various GPIO values, using the BCM numbers for now
DRIVEA0 = 25
DRIVEA1 = 4
STANDBY = 17
DRIVEB0 = 18
DRIVEB1 = 21
A0 = False
A1 = False
B0 = False
B1 = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(DRIVEA0, GPIO.OUT)
GPIO.setup(DRIVEA1, GPIO.OUT)
GPIO.setup(STANDBY, GPIO.OUT)
GPIO.setup(DRIVEB0, GPIO.OUT)
GPIO.setup(DRIVEB1, GPIO.OUT)

# Set all the drives to 'off'
GPIO.output(DRIVEA0, A0)
GPIO.output(DRIVEA1, A1)
GPIO.output(STANDBY, False)
GPIO.output(DRIVEB0, B0)
GPIO.output(DRIVEB1, B1)

# Only start the motors when the inputs go above the following threshold
threshold = 0.60


LeftTrack = 0
RightTrack = 0

# Configure the motors to match the current settings.
def setmotors():
        GPIO.output(DRIVEA0, A0)
        GPIO.output(DRIVEA1, A1)
        GPIO.output(STANDBY, True)
        GPIO.output(DRIVEB0, B0)
        GPIO.output(DRIVEB1, B1)

# Try and run the main code, and in case of failure we can stop the motors
try:
    # Turn on the motors
    GPIO.output(STANDBY, True)

    # This is the main loop
    while True:

        # Check for any queued events and then process each one
        events = pygame.event.get()
        for event in events:
          UpdateMotors = 0

          # Check if one of the joysticks has moved
          if event.type == pygame.JOYAXISMOTION:
            if event.axis == 1:
              LeftTrack = event.value
              UpdateMotors = 1
            elif event.axis == 3:
              RightTrack = event.value
              UpdateMotors = 1

            # Check if we need to update what the motors are doing
            if UpdateMotors:

              # Check how to configure the left motor

              # Move forwards
              if (RightTrack > threshold):
                  A0 = False
                  A1 = True
              # Move backwards
              elif (RightTrack < -threshold):
                  A0 = True
                  A1 = False
              # Stopping
              else:
                  A0 = False
                  A1 = False

              # And do the same for the right motor
              if (LeftTrack > threshold):
                  B0 = False
                  B1 = True
              # Move backwards
              elif (LeftTrack < -threshold):
                  B0 = True
                  B1 = False
              # Otherwise stop
              else:
                  B0 = False
                  B1 = False

              # Now we've worked out what is going on we can tell the
              # motors what they need to do
              setmotors()


except KeyboardInterrupt:
    # Turn off the motors
    GPIO.output(STANDBY, False)
    j.quit()
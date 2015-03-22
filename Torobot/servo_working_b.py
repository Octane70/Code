import serial
import pygame
import time

port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)

# Initialise the pygame library
pygame.init()

# Connect to the first JoyStick
j = pygame.joystick.Joystick(0)
j.init()


print 'Initialized Joystick : %s' % j.get_name()

#Key mappings
PS3_BUTTON_START = 3
PS3_AXIS_LEFT_VERTICAL = 1
PS3_AXIS_RIGHT_VERTICAL = 3
PS3_AXIS_L2 = 12
PS3_AXIS_R2 = 13
PS3_AXIS_L1 = 14
PS3_AXIS_R1 = 15
PS3_AXIS_DPAD_UP = 8
PS3_AXIS_DPAD_RIGHT = 9
PS3_AXIS_DPAD_DOWN = 10
PS3_AXIS_DPAD_LEFT = 11


def servo1_up():
    port.write("#1P2400T100\r\n")
    
def servo1_down():
    port.write("#1P600T100\r\n")
    
def servo2_right():
    port.write("#2P2400T100\r\n")
    
def servo2_left():
    port.write("#2P800T100\r\n")
    
def servos_return():
	port.write("#1P1500T100\r\n")
	port.write("#2P1500T100\r\n")  
 
def processControl(event):

  #Check if one of the joysticks has moved
 if event.type == pygame.JOYAXISMOTION:
       
           
      if event.axis ==PS3_AXIS_L2:
		 print ("servo down") 
		 servo1_down()
		 		          
      if event.axis ==PS3_AXIS_R2:
		 print ("servo up") 
		 servo1_up()				
                          
      if event.axis ==PS3_AXIS_R1:
		 print ("servo right") 
		 servo2_right()
 
      if event.axis ==PS3_AXIS_L1:
		 print ("servo left") 
		 servo2_left()             

      if event.axis ==PS3_AXIS_DPAD_UP:
		 print ("center") 
		 center() 	 
	   		   
try:

    
    while True:
	time.sleep(0.1)
		# Check for any queued events and then process each one
        events = pygame.event.get()
        for event in events:
			processControl(event)
			                 
                   
except KeyboardInterrupt:
       j.quit()
GPIO.cleanup() #cleanup GPIO on KeyboardInterrupt exit

#cleanup GPIO on normal exit
GPIO.cleanup()

import sys
sys.path.append("/home/pi/code/Maestro/modules")
import maestro
import time
import tty
import termios

servo = maestro.Controller()

# Add Min, Mid & Max
servoMin = 1000
servoMid = 6000
servoMax = 9500

# Add servo increments
servoPan = 6000
servostepPan = 500

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

def servo1_left():
  global servoPan
  servoPan += servostepPan
  if servoPan > servoMax:
    servoPan = servoMax
  servo.setAccel(0,0)      #set servo 0 acceleration to 4
  servo.setTarget(0,servoPan)  #set servo to move to center position
  servo.close
    
def servo1_right():
  global servoPan
  servoPan -= servostepPan
  if servoPan < servoMin:
    servoPan = servoMin
  servo.setAccel(0,0)      #set servo 0 acceleration to 4
  servo.setTarget(0,servoPan)  #set servo to move to center position
  servo.close


def servo2_up():
  global servoPan
  servoPan += servostepPan
  if servoPan > servoMax:
    servoPan = servoMax
  servo.setAccel(1,0)      #set servo 0 acceleration to 4
  servo.setTarget(1,servoPan)  #set servo to move to center position
  servo.close
    
def servo2_down():
  global servoPan
  servoPan -= servostepPan
  if servoPan < servoMin:
    servoPan = servoMin
  servo.setAccel(1,0)      #set servo 0 acceleration to 4
  servo.setTarget(1,servoPan)  #set servo to move to center position
  servo.close
  
def servo_return():
  #servoPan = servoMid
  servo.setAccel(0,0)      #set servo 0 acceleration to 4
  servo.setTarget(0,6000)  #set servo to move to center position
  servo.setAccel(1,0)      #set servo 0 acceleration to 4
  servo.setTarget(1,6000)  #set servo to move to center position
  servo.close   
  
print ("d: for right")
print ("a: for left")
print ("w: for up")
print ("s: for down")
         

while True:
	char = getch()
		
	if(char == "a"):
	    servo1_left()
	    print ("Servo Left")
	
	if(char == "d"):
	    servo1_right()
	    print ("Servo Right")

        if(char == "w"):
	    servo2_up()
	    print ("Servo Up")
	
	if(char == "s"):
	    servo2_down()
	    print ("Servo Down")
	    
	if(char == "r"):
	    servo_return()
	    print ("Servo Return")	    
		
	if(char == "x"):
	    print("PROGRAM ENDED")
	    break
	    
	char = ""    	 


servo.close()

             

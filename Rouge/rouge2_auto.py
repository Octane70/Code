import RPi.GPIO as GPIO                    
import time
import rouge2_motors
from rouge2_sensor import Sensor

def forward():
    rouge2_motors.Forward()
    print ("auto forward")
def back():
    rouge2_motors.Reverse()
    print ("auto reverse")
def left():
    rouge2_motors.Left()
    print ("auto left")
def right():
    rouge2_motors.Right()
    print ("auto right")
def stop():
    rouge2_motors.Stop()
    
stop()
count=0
#distance = Sensor()

while True:
 i=0
 avgDistance=0
 for i in range(5):
  distance = Sensor() 
  avgDistance=avgDistance+distance
 avgDistance=avgDistance/5
 print (avgDistance)
 flag=0
 if avgDistance < 15:      #Check whether the distance is within 15 cm range
    count=count+1
    stop()
    time.sleep(1)
    back()
    time.sleep(1.5)
    if (count%3 ==1) & (flag==0):
     right()
     flag=1
    else:
     left()
     flag=0
     time.sleep(1.5)
     stop()
     time.sleep(1)
 else:
     forward()
     flag=0

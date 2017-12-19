import RPi.GPIO as GPIO                    
import time
import rouge2_motors
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                    
TRIG = 8
ECHO = 5
#Ultra sonic sensor in/out
GPIO.setup(TRIG,GPIO.OUT) # initialize GPIO Pin as outputs
GPIO.setup(ECHO,GPIO.IN)  # initialize GPIO Pin as input

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
while True:
 i=0
 avgDistance=0
 for i in range(5):
  GPIO.output(TRIG, False)                   #Set TRIG as LOW
  time.sleep(0.1)                            #Delay
  GPIO.output(TRIG, True)                    #Set TRIG as HIGH
  time.sleep(0.00001)                        #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                   #Set TRIG as LOW
  while GPIO.input(ECHO)==0:                 #Check whether the ECHO is LOW             
    pulse_start = time.time()
  while GPIO.input(ECHO)==1:                 #Check whether the ECHO is HIGH 
    pulse_end = time.time()
  pulse_duration = pulse_end - pulse_start   #time to get back the pulse to sensor
  distance = pulse_duration * 17150          #Multiply pulse duration by 17150 (34300/2) to get distance
  distance = round(distance,2) 
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

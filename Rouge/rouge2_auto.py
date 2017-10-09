import RPi.GPIO as GPIO                    
import time
#Import time library
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                    
TRIG = 8
ECHO = 5
#Ultra sonic sensor in/out
GPIO.setup(TRIG,GPIO.OUT) # initialize GPIO Pin as outputs
GPIO.setup(ECHO,GPIO.IN)  # initialize GPIO Pin as input
#Motor setup
GPIO.setup(23, GPIO.OUT) # purple // 1in
GPIO.setup(24, GPIO.OUT) # blue // 2in
#GPIO.setup(12, GPIO.OUT) # white // 1pwm
#GPIO.setup(18, GPIO.OUT) # grey // 2pwm
GPIO.setup(22, GPIO.OUT) # green // 3in
GPIO.setup(27, GPIO.OUT) # yellow // 4in

#rh = GPIO.PWM(18,120) #white // 1pwm
#rh.start(10) #start right motor at 50% duty cycle
# rh.ChangeDutyCycle(0)

#lh = GPIO.PWM(12,120) #grey // 2pwm
#lh.start(10) #start left motor at 50% duty cycle
# lh.ChangeDutyCycle(0)

#set all Motors to False
GPIO.output(23, False)
GPIO.output(24, False)
GPIO.output(27, False)
GPIO.output(22, False)

#time.sleep(5)

def forward():
    GPIO.output(23, True) #Left Motor // 1ina 
    GPIO.output(24, False)  #Left Motor // 1inb
    GPIO.output(27, False)  #Right Motor // 2ina  
    GPIO.output(22, True) #Right Motor // 2inb
    print ("Forward")
def back():
    GPIO.output(23, False)  #Left Motor // 1ina  
    GPIO.output(24, True) #Left Motor // 1inb
    GPIO.output(27, True) #Right Motor // 2ina   
    GPIO.output(22, False)  #Right Motor // 2inb
    print ("back")
def left():
    GPIO.output(23, False)  #Left Motor // 1ina  
    GPIO.output(24, True) #Left Motor // 1inb
    GPIO.output(27, False)  #Right Motor // 2ina  
    GPIO.output(22, True) #Right Motor // 2inb
    print ("left")
def right():
    GPIO.output(23, True) #Left Motor // 1ina 
    GPIO.output(24, False)  #Left Motor // 1inb
    GPIO.output(27, True) #Right Motor // 2ina   
    GPIO.output(22, False)  #Right Motor // 2inb
    print ("right")
def stop():
    #turn off the motors
    #GPIO.output(12, False)
    #GPIO.output(18, False)
    GPIO.output(23, False)
    GPIO.output(24, False)
    GPIO.output(27, False)
    GPIO.output(22, False)        
stop()
count=0
while True:
 i=0
 avgDistance=0
 for i in range(5):
  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  time.sleep(0.1)                                   #Delay
  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                           #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  while GPIO.input(ECHO)==0:              #Check whether the ECHO is LOW             
    pulse_start = time.time()
  while GPIO.input(ECHO)==1:              #Check whether the ECHO is HIGH 
    pulse_end = time.time()
  pulse_duration = pulse_end - pulse_start #time to get back the pulse to sensor
  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 (34300/2) to get distance
  distance = round(distance,2)                 #Round to two decimal points
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

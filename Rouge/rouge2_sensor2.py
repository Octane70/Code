import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Sensor2
TRIG = 11
ECHO = 6

#print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def Sensor2():

    while True:

          GPIO.output(TRIG, False)
         # print ("Waiting For Sensor To Settle")
          time.sleep(.1)

          GPIO.output(TRIG, True)
          time.sleep(0.00001)
          GPIO.output(TRIG, False)


          while GPIO.input(ECHO)==0:
            pulse_start = time.time()

          while GPIO.input(ECHO)==1:
            pulse_end = time.time()

          pulse_duration = pulse_end - pulse_start

          distance = pulse_duration * 17150

          distance = round(distance, 2)
          return distance     
         # time.sleep(100) 



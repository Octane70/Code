import sys
import os
import subprocess
import RPi.GPIO as gpio
from time import sleep

#CPU Temp min/max in celsius
cpu_fan_min= "25.0"
cpu_fan_max= "30.0"

#Initiate gpio's for relay
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT) # relay 1
gpio.setwarnings(False)

#set relay gpio's to true
gpio.output(17, True) # relay 1

#relay ch1 on and off
def relay_ch1_on():
    gpio.output(17, False) #Relay ch1 on
def relay_ch1_off(): 
    gpio.output(17, True) #Relay ch1 off  

def getTempCPU():
    temp = subprocess.getoutput("/opt/vc/bin/vcgencmd measure_temp")
    initTempPos = str(temp).find("=")
    finishTempPos = str(temp).find("'")
    temp = str(temp)[initTempPos+1:finishTempPos]
    try:
        temp_num = float(temp)
        return temp_num
    except:
        print ("Unable to transform to float")

while True:
    print (getTempCPU())
    cpu_fan_data = getTempCPU()
    cpu_fan_temp = ('%1.0f' % cpu_fan_data)
    if cpu_fan_temp >= cpu_fan_max:   
         relay_ch1_on()
         print ("Case Fan On")
    elif cpu_fan_temp <= cpu_fan_min:
         relay_ch1_off()
         print ("Case Fan Off")
    sleep (1)

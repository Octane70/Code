import os
import sys
import subprocess
sys.path.insert(0, "/home/pi/BlueControl/bluepad")
from bluepad.btcomm import BluetoothServer
from signal import pause
import RPi.GPIO as GPIO
import time

#Control GPIO's
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Door Lock
GPIO.setup(17,GPIO.OUT) 
GPIO.output(17,True)
#Door Unlock
GPIO.setup(22,GPIO.OUT) 
GPIO.output(22,True)
#Lights On/Off
GPIO.setup(23,GPIO.OUT) 
GPIO.output(23,True)
#Auto Start/Stop
GPIO.setup(27,GPIO.OUT) 
GPIO.output(27,True)

#Data to Bluetooth server        
def data_received(data):
    control_mode(data)
    #shutdown(data)
    #restart(data)

#Restart Controls RPI
#def restart(command):
    #if command == "9":
       #os.system("sudo reboot")    

#Shutdown Controls RPI
#def shutdown(command):
    #if command == "10":
       #os.system("sudo poweroff")
  
#Control Mode
def control_mode(command):
    
    #Doors Lock
    if command == "1":
         GPIO.output(17, False)
    elif command == "2":
         GPIO.output(17, True)

    #Doors Unlock
    elif command == "3":
         GPIO.output(22, False)
    elif command == "4":
         GPIO.output(22, True)

    #Light Switch
    elif command == "5":
         GPIO.output(23, False)
    elif command == "6":
         GPIO.output(23, True)

    #Auto Start/Stop
    elif command == "7":
         GPIO.output(27, False)
    elif command == "8":
         GPIO.output(27, True)

BluetoothServer(data_received)
        
#except KeyboardInterrupt:
#GPIO.output(17, True)
#GPIO.output(22, True)
#GPIO.output(23, True)
#GPIO.output(27, True)


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
#Doord Lock/Unlock
GPIO.setup(17,GPIO.OUT) 
GPIO.output(17,False)
#Lights On/Off
GPIO.setup(22,GPIO.OUT) 
GPIO.output(22,True)
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
         rouge2_motors.Forward()
    elif command == "2":
         rouge2_motors.Stop()

    #Doors Unlock
    elif command == "3":
         rouge2_motors.Reverse()
    elif command == "4":
         rouge2_motors.Stop()

    #Dpad Left
    elif command == "5":
         rouge2_motors.Left()
    elif command == "6":
         rouge2_motors.Stop()

    #Auto Start/Stop
    elif command == "7":
         rouge2_motors.Right()
    elif command == "8":
         rouge2_motors.Stop()

BluetoothServer(data_received)
        
#except KeyboardInterrupt:
GPIO.output(16, True)
GPIO.output(26, True)
GPIO.cleanup()

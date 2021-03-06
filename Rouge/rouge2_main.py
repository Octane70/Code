import os
import sys
import subprocess
sys.path.insert(0, "/home/pi/rouge/bluepad")
from bluepad.btcomm import BluetoothServer
from signal import pause
import RPi.GPIO as GPIO
from rouge2_sensor1 import Sensor1
from rouge2_sensor2 import Sensor2
import rouge2_motors
import alsaaudio
import time
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#RGB LED
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT) # Green
GPIO.output(16,False)    # Green set to High
GPIO.setup(26,GPIO.OUT) # Blue
GPIO.output(26,True)    # Blue set to High

# <------Start Oled Configuration------>
RST = None
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
padding = -2
top = padding
bottom = height-padding
x = 0
font = ImageFont.load_default()    

# IP String
cmd = "hostname -I | cut -d\' \' -f1"
IP = subprocess.check_output(cmd, shell = True )
#<------End Oled Configuration------>#

#Globals
auto_process = None
volume = alsaaudio.Mixer('PCM')
#vol = m.getvolume()
vol = 100

#Sound files
mp3_file1 = ('sounds/R2D2-yeah.mp3')
mp3_file2 = ('sounds/beverly_hills_cop.mp3')
mp3_online = ('sounds/onlinef.mp3')

subprocess.Popen(["mpg123",mp3_online])

#Auto mode on and off functions
def rouge2_auto_on():
    global auto_process
    if auto_process == None:
       rouge2_motors.Stop()
       auto_process = subprocess.Popen(["python3","rouge2_auto.py"])

def rouge2_auto_off():
    global auto_process
    if auto_process != None:
       auto_process.terminate()
       rouge2_motors.Stop()
       auto_process = None

#Data to Bluetooth server        
def data_received(data):
    auto_manual(data)
    manual_mode(data)
    shutdown(data)
    vol_ctrl(data)
    sound_ctrl(data)
    camera(data) 

#Auto and manual buttons
def auto_manual(command):
    if command == "9":
        GPIO.output(26, True)
        GPIO.output(16, False)
        rouge2_auto_off()
        print ("Green On")
    elif command == "10":
         GPIO.output(16, True)
         GPIO.output(26, False)
         rouge2_auto_on()
         print ("Blue On")

#Shutdown rouge2
def shutdown(command):
    if command == "12":
       rouge2_motors.Stop()
       GPIO.cleanup()
       disp.clear()
       disp.display()
       os.system("sudo poweroff")

#Sound effect on and off
def sound_ctrl(command):
    if command == "13":
       subprocess.Popen(["mpg123",mp3_file2])
       print ("Sound on")
    elif command == "14":
       subprocess.call(['killall', 'mpg123'])
       print ("Sound off")

#Speaker volume control
def vol_ctrl(command):
    global vol
    volume.setvolume(vol)
    if command == "15":
       if (vol < 100):
           vol = vol + 1
           print (vol)
       else:
            return
    elif command == "16":
       if (vol > 0):
           vol = vol - 1
           print (vol)
       else:
            return
   
#Manual motor control
def manual_mode(command):
    global auto_process
    if auto_process !=None:
       return
    #Dpad Forward
    if command == "1":
         rouge2_motors.Forward()
    elif command == "2":
         rouge2_motors.Stop()

        #Dpad Reverse
    elif command == "3":
         rouge2_motors.Reverse()
    elif command == "4":
         rouge2_motors.Stop()

    #Dpad Left
    elif command == "5":
         rouge2_motors.Left()
    elif command == "6":
         rouge2_motors.Stop()

    #Dpad Right
    elif command == "7":
         rouge2_motors.Right()
    elif command == "8":
         rouge2_motors.Stop()

#capture picture
def camera (command):
    if command == "18":
       subprocess.Popen(["python3","camera.py"])

BluetoothServer(data_received)

try:
    while True:
         
        # Draw a black filled box to clear the image.
         draw.rectangle((0,0,width,height), outline=0, fill=0)
         def sonic_sensor1():
             if (GPIO.input(16) == False): #Green Led On
                 range1 = Sensor1()
                 return "Dist.front: %scm" % str(range1)
                 print (range1)
                 time.sleep(100)
             else:
                 return
         
         def sonic_sensor2():
             if (GPIO.input(16) == False): #Green Led On
                 range2 = Sensor2()
                 return "Dist.rear: %scm" % str(range2)
                 print (range2)
                 time.sleep(100)
             else:
                 return

         draw.text((x, top),       "IP: " + str(IP),  font=font, fill=255)
         draw.text((x, top+16),    "Rouge2 is online", font=font, fill=255)

         if (GPIO.input(16) == False): #Green Led On
              draw.text((x, top+25),     "Manual mode", font=font, fill=255)
         else: 
             draw.text((x, top+25),     "  ", font=font, fill=255)

         if (GPIO.input(26) == False): #Blue Led off
              draw.text((x, top+25),     "Autonomous mode", font=font, fill=255)
         else:
             draw.text((x, top+25),     " ", font=font, fill=255)

         # Front and rear ultra sonic sensors
         #Front sensor
         if (GPIO.input(16) == False): #Green Led On
             draw.text((x, top+35),   sonic_sensor1(), font=font, fill=255)
         else:
             draw.text((x, top+35),     " ", font=font, fill=255)

         #Rear sensor
         if (GPIO.input(16) == False): #Green Led On
             draw.text((x, top+45),   sonic_sensor2(), font=font, fill=255)
         else:
             draw.text((x, top+45),     " ", font=font, fill=255)

         # Display image.
         disp.image(image)
         disp.display()
         time.sleep(.1)

#confirmation()

except KeyboardInterrupt:
       GPIO.output(16, True)
       GPIO.output(26, True)
       GPIO.cleanup()
       disp.clear()
       disp.display()
      

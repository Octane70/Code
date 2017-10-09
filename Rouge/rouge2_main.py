from bluedot import BlueDot
import RPi.GPIO as GPIO
import rouge2_sensor
from signal import pause
import time
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess

bd= BlueDot()

#ultrasonic = DistanceSensor(ECHO=17, TRIG=4)
#RGB LED
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setup(6,GPIO.OUT) # Red
#GPIO.output(6,True)     # Red set to High
GPIO.setup(16,GPIO.OUT) # Green
GPIO.output(16,False)    # Green set to High
GPIO.setup(26,GPIO.OUT) # Blue
GPIO.output(26,True)    # Blue set to High

# <------Start Oled Configuration------>
RST = None     # on the PiOLED this pin isnt used
# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
# Initialize library.
disp.begin()
# Clear display.
disp.clear()
disp.display()
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0
# Load default font.
font = ImageFont.load_default()    

# IP String
cmd = "hostname -I | cut -d\' \' -f1"
IP = subprocess.check_output(cmd, shell = True )
#<------End Oled Configuration------>

def auto_manual(channel):
    if (GPIO.input(16) == False): #Green Led On
        GPIO.output(16, True)
        GPIO.output(26, False)
        print ("Blue On")
    elif (GPIO.input(26) == False): #Blue Led On
          GPIO.output(26, True)
          GPIO.output(16, False)
          print ("Green On")
    else:
          GPIO.output(16, False)
          print ("Green 0n")

bd.when_pressed = auto_manual

try:
    while True:

        # Draw a black filled box to clear the image.
         draw.rectangle((0,0,width,height), outline=0, fill=0)
         def sonic_sensor(): 
             range = rouge2_sensor.Sensor()
             return "Distance: %scm" % str(range)
             print (range)

         draw.text((x, top),       "IP: " + str(IP),  font=font, fill=255)
         draw.text((x, top+16),    "Rouge2 is online", font=font, fill=255)

         if (GPIO.input(16) == False): #Green Led Off
              draw.text((x, top+25),     "Manual mode", font=font, fill=255)
         else: 
             draw.text((x, top+25),     "  ", font=font, fill=255)

         if (GPIO.input(26) == False): #Blue Led off
              draw.text((x, top+25),     "Autonomous mode", font=font, fill=255)
         else:
             draw.text((x, top+25),     " ", font=font, fill=255)

         #range = distance.Sensor()

         draw.text((x, top+35),    sonic_sensor(), font=font, fill=255)

         # Display image.
         disp.image(image)
         disp.display()
         time.sleep(.1)

except KeyboardInterrupt:
       GPIO.output(16, True)
       GPIO.output(26, True)
       GPIO.cleanup()
       disp.clear()
       disp.display()

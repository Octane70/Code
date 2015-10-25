import sys
import RPi.GPIO as GPIO
import time
import tty
import termios

# Variables

delay = 0.0055
steps = 100

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Enable GPIO pins for  ENA and ENB for stepper

#enable_a = 18
#enable_b = 22

# Enable pins for IN1-4 to control step sequence

coil_A_1_pin = 23
coil_A_2_pin = 24
coil_B_1_pin = 4
coil_B_2_pin = 17

# Set pin states

#GPIO.setup(enable_a, GPIO.OUT)
#GPIO.setup(enable_b, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# Set ENA and ENB to high to enable stepper

#GPIO.output(enable_a, True)
#GPIO.output(enable_b, True)

# Function for step sequence

def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

# loop through step sequence based on number of steps
def forward():
    for i in range(0, steps):
        setStep(1,0,1,0)
        time.sleep(delay)
        setStep(0,1,1,0)
        time.sleep(delay)
        setStep(0,1,0,1)
        time.sleep(delay)
        setStep(1,0,0,1)
        time.sleep(delay)

# Reverse previous step sequence to reverse motor direction

#for i in range(0, steps):
    #setStep(1,0,0,1)
    #time.sleep(delay)
    #setStep(0,1,0,1)
    #time.sleep(delay)
    #setStep(0,1,1,0)
    #time.sleep(delay)
    #setStep(1,0,1,0)
    #time.sleep(delay)

while True:
	char = getch()
		
	if(char == "a"):
	    forward()
	    print ("Stepper Forward")
	
	if(char == "x"):
	    print("PROGRAM ENDED")
	    break
	    
	char = "" 

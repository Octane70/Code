import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(16, GPIO.OUT) ## Setup GPIO Pin 11(motor a enable) to OUT
GPIO.setup(18, GPIO.OUT)  ## Setup GPIO Pin 11(motor b enable) to OUT
GPIO.setup(32, GPIO.OUT) ## Setup GPIO Pin 11(motor a control) to OUT
GPIO.setup(12, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setwarnings(False)

GPIO.output(32, True)        ## disable motor l
GPIO.output(12, True)        ## disable motor r

l=GPIO.PWM(32,120)          ## frequency 50
r=GPIO.PWM(12,120)          ## frequency 50
l.start(5)
r.start(5)

pause_time = 3

try:
    while True:
           GPIO.output(16, True)   ## dont run motor a
           GPIO.output(18, False)      ## dont run motor a
           l.ChangeDutyCycle(10)     ## duty cycle 10%
           time.sleep(pause_time)
           GPIO.output(15, False)
           GPIO.output (11, True)
           r. ChangeDutyCycle(10)
           time.sleep(pause_time)
           
except KeyboardInterrupt:
     pass
r.stop()
l.stop()
GPIO.cleanup()

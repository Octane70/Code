import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(18, GPIO.OUT) ## Setup GPIO Pin 11(motor a enable) to OUT
GPIO.setup(23, GPIO.OUT)  ## Setup GPIO Pin 11(motor b enable) to OUT
GPIO.setup(22, GPIO.OUT) ## Setup GPIO Pin 11(motor a control) to OUT
GPIO.setup(27, GPIO.OUT)  ## Setup GPIO Pin 11(motor a control) to OUT
GPIO.setup(25, GPIO.OUT)   ## Setup GPIO Pin 11(motor b control) to OUT
GPIO.setup(24, GPIO.OUT)    ## Setup GPIO Pin 11(motor b control) to OUT
GPIO.output(18, True)        ## disable motor a
GPIO.output(23, False)          ## enable motor b
p=GPIO.PWM(18,100)          ## frequency 50
p.start(1)
try:
    while True:
           GPIO.output(22, False)   ## dont run motor a
           GPIO.output(27, True)      ## dont run motor a
           GPIO.output(25, False)        ##  run motor b
           GPIO.output(24, False)         ##  run motor b
           p.ChangeDutyCycle(30)     ## duty cycle 10%
except KeyboardInterrupt:
     pass
p.stop()
GPIO.cleanup()

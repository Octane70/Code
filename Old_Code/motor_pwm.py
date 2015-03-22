import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(17, GPIO.OUT) ## Setup GPIO Pin 11(motor a enable) to OUT
GPIO.setup(22, GPIO.OUT)  ## Setup GPIO Pin 11(motor b enable) to OUT
GPIO.setup(27, GPIO.OUT) ## Setup GPIO Pin 11(motor a control) to OUT
GPIO.output(17, True)        ## disable motor a
p=GPIO.PWM(17,100)          ## frequency 50
p.start(1)

pause_time = 1

try:
    while True:
           GPIO.output(22, True)   ## dont run motor a
           GPIO.output(27, False)      ## dont run motor a
           p.ChangeDutyCycle(100)     ## duty cycle 10%
           time.sleep(pause_time)
           #GPIO.output(23, False)
           #GPIO.output (24, True)
           #p. ChangeDutyCycle(50)
           #time.sleep(pause_time)
           
except KeyboardInterrupt:
     pass
p.stop()
GPIO.cleanup()

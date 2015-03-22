import RPi.GPIO as GPIO
from time import sleep  

GPIO.setmode(GPIO.BCM)  
#Set output pins
GPIO.setup(17, GPIO.OUT) # set pin 17 as 1PWM output for motor1
GPIO.setup(23, GPIO.OUT) # set pin 23 as 2PWM output for motor2
GPIO.setup(22, GPIO.OUT) # set pin 22 as 1INa output for motor1 
GPIO.setup(27, GPIO.OUT) # set pin 27 as 1INb output for motor1
GPIO.setup(25, GPIO.OUT) # set pin 25 as 2INa output for motor2
GPIO.setup(24, GPIO.OUT) # set pin 24 as 2INb output for motor2 
#Set PWM pins
motor1 = GPIO.PWM(17, 100) # create object motor1 for PWM on port 17 at 100 Hertz
motor2 = GPIO.PWM(23, 100) # create object motor2 for PWM on port 23 at 100 Hertz

motor1.start(100)            # start motor1 on 0 percent duty cycle (off)
motor2.start(100)          # start motor2 fully on (100%)

pause_time = 1.00          # you can change this to slow down/speed up

try:
    while True:
        for i in range(0,101):      # 101 because it stops when it finishes 100
            motor1.ChangeDutyCycle(i)
            motor2.ChangeDutyCycle(100 - i)
            sleep(pause_time)
        for i in range(100,-1,-1):      # from 100 to zero in steps of -1
            motor1.ChangeDutyCycle(i)
            motor2.ChangeDutyCycle(100 - i)
            sleep(pause_time)

except KeyboardInterrupt:
    motor1.stop()           # stop the motor1 PWM output
    motor2.stop()           # stop the motor2 PWM output
    GPIO.cleanup()          # clean up GPIO on CTRL+C exit


import serial
import time

class ServoController:
    def __init__(self):
        usbPort = '/dev/ttyACM0'
        self.sc = serial.Serial(usbPort)

    def closeServo(self):
        self.sc.close()

    def setAngle(self, n, angle):
        if angle > 180 or angle <0:
           angle=90
        byteone=int(254*angle/180)
        bud=chr(0xFF)+chr(n)+chr(byteone)
        self.sc.write(bud)

    def setPosition(self, servo, position):
        position = position * 4
        poslo = (position & 0x7f)
        poshi = (position >> 7) & 0x7f
        chan  = servo &0x7f
        data =  chr(0xaa) + chr(0x0c) + chr(0x04) + chr(chan) + chr(poslo) + chr(poshi)
        self.sc.write(data)

    def getPosition(self, servo):
        chan  = servo &0x7f
        data =  chr(0xaa) + chr(0x0c) + chr(0x10) + chr(chan)
        self.sc.write(data)
        w1 = ord(self.sc.read())
        w2 = ord(self.sc.read())
        return w1, w2

    def getErrors(self):
        data =  chr(0xaa) + chr(0x0c) + chr(0x21)
        self.sc.write(data)
        w1 = ord(self.sc.read())
        w2 = ord(self.sc.read())
        return w1, w2

    def triggerScript(self, subNumber):
        data =  chr(0xaa) + chr(0x0c) + chr(0x21) + chr(0x27) + chr(subNumber)
        self.sc.write(data)

# MAIN
         
Maestro = ServoController()

iterations = 2

while(iterations > 0):
    for chan in range(0,3):
        for pos in range(0, 180):
            Maestro.setAngle(chan, pos)
            time.sleep(.002)
            print Maestro.getPosition(chan), Maestro.getErrors()

    for chan in range(0,3):
        for pos in range(180, 0, -1):
            Maestro.setAngle(chan, pos)
            time.sleep(.002)
            print Maestro.getPosition(chan)

    e1, e2 = Maestro.getErrors()
    if e1 != 0 or e2 != 0:
       print e1, e2
       break

    iterations = iterations - 1

    print "Trigger Script"
    Maestro.triggerScript(0)
    
time.sleep(2)
Maestro.closeServo()

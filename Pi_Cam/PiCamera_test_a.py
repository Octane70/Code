import sys
import picamera
import tty
import termios

camera = picamera.PiCamera()


camera.hflip = True
camera.vflip = True

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

def camera_start():
  camera.start_preview() 

def camera_stop():
  camera.stop_preview()
  
while True:
	char = getch()
		
	if(char == "a"):
	    camera_start()
	    print ("Camera on")
	
	if(char == "d"):
	    camera_stop()
	    print ("Camera off")

	if(char == "x"):
	    print("PROGRAM ENDED")
	    break
	    
	char = ""  

import sys
sys.path.append("/home/pi/code/Maestro/modules")
import maestro
import numpy as np
import cv2
import Tkinter as tk
import Image, ImageTk

#servo = maestro.Controller()

# Add Min, Mid & Max
servoMin = 1000
servoMid = 6000
servoMax = 9500

# Add servo increments
servoPan = 6000
servostepPan = 500

#Main GUI Window
window = tk.Tk()
#Title
window.wm_title("Motion Cam 1")

#Capture window
imageFrame = tk.Frame(window, borderwidth=5, relief="ridge", width=800, height=800)
imageFrame.grid(row=0, column=0, columnspan=1, rowspan=1, padx=10, pady=2)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)
def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

#Control Window 
controlFrame = tk.Frame(window, borderwidth=5, relief="ridge", width=650, height=100)
controlFrame.grid(row=1, column=0, padx=10, pady=2)

#Labels
L1 = tk.Label(controlFrame, text="Tracking Mode:")
L1.grid(row=1, column=0, columnspan=2, rowspan=1, padx=5, pady=5)
L2 = tk.Label(controlFrame, text="Manual Mode:")
L2.grid(row=3, column=0, columnspan=2, rowspan=1, padx=5, pady=5)

#Frames
F1 = tk.Frame(controlFrame, borderwidth=5, bg="red", relief="ridge", width=25, height=25)
F1.grid(row=2, column=1, padx=5, pady=5)
F2 = tk.Frame(controlFrame, borderwidth=5, bg="green", relief="ridge", width=25, height=25)
F2.grid(row=4, column=1, padx=5, pady=5)

#Camera Mode:
def track_mode():
    print "Track Mode"

B6=tk.Button(controlFrame, text="OFF", command=track_mode, width=4, height=1)
B6.grid(row=2, column=0, padx=5, pady=5)

def manual_mode():
    print "Manual Mode"

B7=tk.Button(controlFrame, text="ON", command=manual_mode, width=4, height=1)
B7.grid(row=4, column=0, padx=5, pady=5)

#Servo Functions:

#Servo Up Button
def camera_up():
  global servoPan
  servoPan += servostepPan
  if servoPan > servoMax:
    servoPan = servoMax
  servo.setAccel(1,0)      #set servo 0 acceleration to 4
  servo.setTarget(1,servoPan)  #set servo to move to center position
  servo.close
  print "Camera up"
    
B1=tk.Button(controlFrame, text="UP", command=camera_up, width=4, height=1)
B1.grid(row=1, column=7, padx=5, pady=5)

#Servo Home Button
def camera_home():
  #servoPan = servoMid
  servo.setAccel(0,0)      #set servo 0 acceleration to 4
  servo.setTarget(0,6000)  #set servo to move to center position
  servo.setAccel(1,0)      #set servo 0 acceleration to 4
  servo.setTarget(1,6000)  #set servo to move to center position
  servo.close  
  print "Camera Home"

B2=tk.Button(controlFrame, text="HOME", command=camera_home, width=4, height=1)
B2.grid(row=2, column=7, padx=5, pady=5)

#Servo Down Button
def camera_down():
  global servoPan
  servoPan -= servostepPan
  if servoPan < servoMin:
    servoPan = servoMin
  servo.setAccel(1,0)      #set servo 0 acceleration to 4
  servo.setTarget(1,servoPan)  #set servo to move to center position
  servo.close
  print "Camera Down"
    
B3=tk.Button(controlFrame, text="DOWN", command=camera_down, width=4, height=1)
B3.grid(row=3, column=7, padx=5, pady=5)

#Servo Left Button
def camera_left():
  global servoPan
  servoPan += servostepPan
  if servoPan > servoMax:
    servoPan = servoMax
  servo.setAccel(0,0)      #set servo 0 acceleration to 4
  servo.setTarget(0,servoPan)  #set servo to move to center position
  servo.close
  print "Camera Left"

B4=tk.Button(controlFrame, text="LEFT", command=camera_left, width=4, height=1)
B4.grid(row=2, column=6, padx=5, pady=5)

#Servo Right Button
def camera_right():
  global servoPan
  servoPan -= servostepPan
  if servoPan < servoMin:
    servoPan = servoMin
  servo.setAccel(0,0)      #set servo 0 acceleration to 4
  servo.setTarget(0,servoPan)  #set servo to move to center position
  servo.close
  print "Camera Right"
    
B5=tk.Button(controlFrame, text="RIGHT", command=camera_right, width=4, height=1)
B5.grid(row=2, column=8, padx=5, pady=5)

#Close Camera Button
#def camera_close():
    #print "Camera Close"
    
#B6=tk.Button(buttonFrame, text="Close", command=camera_close, width=4, height=1)
#B6.grid(row=0, column=0, padx=10, pady=2)
   
show_frame()  #Display 2
window.mainloop()  #Starts GUI

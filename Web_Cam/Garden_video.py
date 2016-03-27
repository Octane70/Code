import numpy as np
import cv2
import Tkinter as tk
import Image, ImageTk

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Garden Camera")

#Graphics window
imageFrame = tk.Frame(window, width=800, height=800)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

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

#Button Window 
buttonFrame = tk.Frame(window, borderwidth=5, relief="ridge", width=650, height=100)
buttonFrame.grid(row = 2, column=0, padx=10, pady=2)

#Servo Control:
#Servo Up Button
def camera_up():
    print "Camera up"
    
B1=tk.Button(buttonFrame, text="UP", command=camera_up, width=4, height=1)
B1.grid(row=1, column=1, padx=10, pady=2)

#Servo Home Button
def camera_home():
    print "Camera Home"

B2=tk.Button(buttonFrame, text="HOME", command=camera_home, width=4, height=1)
B2.grid(row=2, column=1, padx=10, pady=2)

#Servo Down Button
def camera_down():
    print "Camera Down"
    
B3=tk.Button(buttonFrame, text="DOWN", command=camera_down, width=4, height=1)
B3.grid(row=3, column=1, padx=10, pady=2)

#Servo Left Button
def camera_left():
    print "Camera Left"

B4=tk.Button(buttonFrame, text="LEFT", command=camera_left, width=4, height=1)
B4.grid(row=2, column=0, padx=10, pady=2)

#Servo Right Button
def camera_right():
    print "Camera Right"
    
B5=tk.Button(buttonFrame, text="RIGHT", command=camera_right, width=4, height=1)
B5.grid(row=2, column=2, padx=10, pady=2)

#Close Camera Button
def camera_close():
    print "Camera Close"
    
B5=tk.Button(buttonFrame, text="Close", command=camera_close, width=4, height=1)
B5.grid(row=0, column=0, padx=10, pady=2)

show_frame()  #Display 2
window.mainloop()  #Starts GUI

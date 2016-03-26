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



#Slider window (slider controls stage position)
buttonFrame = tk.Frame(window, borderwidth=5, relief="ridge", width=650, height=100)
buttonFrame.grid(row = 600, column=0, padx=10, pady=2)


def camera_up():
    print "Camera up"
    
#Buttons
B1=tk.Button(buttonFrame, text="UP", command=camera_up, width=4, height=1)
B1.grid(row=1, column=1, padx=10, pady=2)

show_frame()  #Display 2
window.mainloop()  #Starts GUI

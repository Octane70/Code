import numpy as np
import cv2
#import Tkinter as tk
import Image, ImageTk

##Set up GUI
#window = tk.Tk()  #Makes main window
#window.wm_title("Digital Microscope")
#window.config(background="#FFFFFF")

#Graphics window
#imageFrame = tk.Frame(window, width=800, height=800)
#imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
#lmain = tk.Label(imageFrame)
#lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)
num= 0
def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
    num+= 1    
print(num)

show_frame()  #Display 2
window.mainloop()  #Starts GUI

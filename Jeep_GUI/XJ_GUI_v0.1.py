from tkinter import *

root = Tk()
root.geometry("800x480+0+0")
root.minsize(800,480)
root.maxsize(800,480)
root.title('Jeep XJ GUI v0.1')

#---Window Tabs---#
window1 = Frame(root, borderwidth=5, relief="ridge", width=800, height=424)#Window1
window1.grid(row=1, column=0, columnspan=800, rowspan=1, sticky=NW) #Window1 Default
window2 = Frame(root, borderwidth=5, relief="ridge", width=800, height=424) #Window2
window3 = Frame(root, borderwidth=5, relief="ridge", width=800, height=424) #Window3
window4 = Frame(root, borderwidth=5, relief="ridge", width=800, height=424) #Window4

window1.grid_propagate(False) # Prevent window1 from resizing
window2.grid_propagate(False) # Prevent window2 from resizing
window3.grid_propagate(False) # Prevent window3 from resizing
window4.grid_propagate(False) # Prevent window4 from resizing


#L2 = Label(window2, text="Camera").grid(row=1, column=0, sticky=W)
L3 = Label(window3, text="Jeep Diagnostics").grid(row=1, column=0, sticky=W)
L4 = Label(window4, text="RPI Zero").grid(row=1, column=0, sticky=W)

def Window_1():
    window2.grid_remove()
    window3.grid_remove()
    window4.grid_remove()
    window1.grid(row=1, column=0, columnspan=800, rowspan=1, sticky=NW) #Window1
        
B1=Button(root, text=" Jeep Controls", command= Window_1, width=15, height=3)
B1.grid(row=0, column=0, sticky=NW)

def Window_2():
    window1.grid_remove()
    window3.grid_remove()
    window4.grid_remove()
    window2.grid(row=1, column=0, columnspan=800, rowspan=1, sticky=NW) #Window2

B1=Button(root, text="Camera", command= Window_2, width=15, height=3)
B1.grid(row=0, column=1, sticky=NW)

def Window_3():
    window1.grid_remove()
    window2.grid_remove()
    window4.grid_remove()
    window3.grid(row=1, column=0, columnspan=800, rowspan=2, sticky=NW) #Window3
        
B1=Button(root, text="Jeep Diagnostics", command= Window_3, width=15, height=3)
B1.grid(row=0, column=3, sticky=NW)

def Window_4():
    window1.grid_remove()
    window2.grid_remove()
    window3.grid_remove()
    window4.grid(row=1, column=0, columnspan=800, rowspan=2, sticky=NW) #Window4
    
B1=Button(root, text="RPI Zero", command= Window_4, width=15, height=3)
B1.grid(row=0, column=4, sticky=NW)

#--Window1 Layout--#
#Window1 Labels
W1L1 = Label(window1, text="Door Locks:").grid(row=1, column=0, columnspan=2, sticky=W)
W1L1 = Label(window1, text="Vehicle Start:").grid(row=4, column=0, columnspan=2, sticky=W)

#Window1 Frames
W1F1 = Frame(window1, borderwidth=3, bg="yellow", relief="ridge", width=65, height=25)
W1F1.grid(row=2, column=0, columnspan=1, rowspan=1, sticky=W)
W1F2 = Frame(window1, borderwidth=3, bg="yellow", relief="ridge", width=65, height=25)
W1F2.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=W) 
W1F3 = Frame(window1, borderwidth=3, bg="yellow", relief="ridge", width=65, height=25)
W1F3.grid(row=5, column=0, columnspan=1, rowspan=1, sticky=W)
W1F4 = Frame(window1, borderwidth=3, bg="yellow", relief="ridge", width=65, height=25)
W1F4.grid(row=5, column=1, columnspan=1, rowspan=1, sticky=W)

#Window1 Buttons
def Door_Lock():
    print ("Doors Locked")
    
B1=Button(window1, text="Lock", command= Door_Lock, width=8, height=2)
B1.grid(row=3, column=0, sticky=NW)

def Door_UnLock():
    print ("Doors Unlocked")
    
B2=Button(window1, text="UnLock", command= Door_UnLock, width=8, height=2)
B2.grid(row=3, column=1, sticky=NW)

def Car_Start():
    print ("Car Start")
    
B3=Button(window1, text="Start", command= Car_Start, width=8, height=2)
B3.grid(row=6, column=0, sticky=NW)

def Car_Stop():
    print ("Car Stop")
    
B4=Button(window1, text="Stop", command= Car_Stop, width=8, height=2)
B4.grid(row=6, column=1, sticky=NW)

#--Window2 Layout--#
#Window2 Frames
W2F1 = Frame(window2, borderwidth=5, relief="ridge", width=640, height=415) # Camera Frame
W2F1.grid(row=1, column=0, sticky=NW) # Camera Frame grid
W2F1.grid_propagate(False) # Prevent Camera Frame from resizing
W2F2 = Frame(window2, borderwidth=5, relief="ridge", width=150, height=415) # Window2/Frame2
W2F2.grid(row=1, column=1, sticky=NW) # Window2/Frame2 grid
W2F2.grid_propagate(False) # Prevent Window2/Frame2 from resizing
W2F3 = Frame(W2F2, borderwidth=3, relief="ridge", width=65, height=25) # Capture LED
W2F3.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=W)
W2F3.config(bg = "green")
W2F4 = Frame(W2F2, borderwidth=3, bg="green", relief="ridge", width=65, height=25) # Record LED
W2F4.grid(row=2, column=2, columnspan=1, rowspan=1, sticky=W)

#Window2 Buttons
def Capture_Frame():
    W2F3.config(bg = "red")
    print ("Capture")
    root.after(200, lambda: W2F3.config(bg = "green" ))
        
B4=Button(W2F2, text="Capture", command= Capture_Frame, width=8, height=2)
B4.grid(row=1, column=1, sticky=NW)

def Record_Frame():
    print ("Record")
    
B4=Button(W2F2, text="Record", command= Record_Frame, width=8, height=2)
B4.grid(row=2, column=1, sticky=NW)

def Record_Stop():
    print ("Stop Record")
    
B4=Button(W2F2, text="Stop", command= Record_Stop, width=8, height=2)
B4.grid(row=3, column=1, sticky=NW)

root.mainloop() 
#gpio.cleanup()	

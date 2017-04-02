from tkinter import *

root = Tk()
root.geometry("800x480+0+0")
root.minsize(800,480)
root.maxsize(800,480)
root.title('Jeep XJ GUI v0.1')

window1 = Frame(root, borderwidth=5, relief="ridge", width=800, height=424)#Window1
window1.grid(row=1, column=0, columnspan=800, rowspan=1, sticky=NW) #Window1 Default
window2 = Frame(root, borderwidth=5, relief="ridge", width=800, height=424) #Window2
window3 = Frame(root, borderwidth=5, relief="ridge", width=800, height=424) #Window3

window1.grid_propagate(False) # Prevent window1 from resizing
window2.grid_propagate(False) # Prevent window2 from resizing
window3.grid_propagate(False) # Prevent window3 from resizing

L1 = Label(window1, text="Controls").grid(row=1, column=0, sticky=W)
L2 = Label(window2, text="Camera").grid(row=1, column=0, sticky=W)
L3 = Label(window3, text="Diagnostics").grid(row=1, column=0, sticky=W)

def Window_1():
    window2.grid_remove()
    window3.grid_remove()
    window1.grid(row=1, column=0, columnspan=800, rowspan=1, sticky=NW) #Window1
        
B1=Button(root, text="Controls", command= Window_1, width=15, height=3)
B1.grid(row=0, column=0, sticky=NW)

def Window_2():
    window1.grid_remove()
    window3.grid_remove()
    window2.grid(row=1, column=0, columnspan=800, rowspan=1, sticky=NW) #Window2

B1=Button(root, text="Camera", command= Window_2, width=15, height=3)
B1.grid(row=0, column=1, sticky=NW)

def Window_3():
    window1.grid_remove()
    window2.grid_remove()
    window3.grid(row=1, column=0, columnspan=800, rowspan=2, sticky=NW) #Window3
    
B1=Button(root, text="Diagnostics", command= Window_3, width=15, height=3)
B1.grid(row=0, column=3, sticky=NW)










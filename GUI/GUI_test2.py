import sys
from Tkinter import *
myApp = Tk()
myApp.title('My App')
myApp.geometry('400x400+350+340')
label = Label(text='My Label', fg ='red', bg = 'white').grid(row=0,column=0,sticky=E)
label = Label(text='My Label', fg ='red', bg = 'white').grid(row=1,column=0,sticky=E)
label = Label(text='My Label', fg ='red', bg = 'white').grid(row=0,column=1,sticky=E)
myApp.mainloop()

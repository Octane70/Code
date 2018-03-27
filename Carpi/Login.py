from tkinter import*
import os

login = Tk()
login.title('XJ Login')


# Globals
pin = '' # empty string

# Entry
E1 = Entry(login)
E1.grid(row=0, column=0, columnspan=3, ipady=5)

# --- functions ---

def entry(value):

    # inform function to use external/global variable
    global pin

    if value == '<':
        # remove last number from `pin`
        pin = pin[:-1]
        # remove all from `entry` and put new `pin`
        E1.delete('0', 'end')
        E1.insert('end', pin)

    elif value == 'E':
        # check pin

        if pin == "1234":
            os.system("sudo python3 Carpi.py")
            login.destroy()
            print("PIN OK")
        else:
            print("PIN ERROR!", pin)
            # clear `pin`
            pin = ''
            # clear `entry`
            E1.delete('0', 'end')

    else:
        # add number to pin
        pin += value
        # add number to `entry`
        E1.insert('end', value)

    print("Current:", pin)

# --- main ---

keys = [
    ['1', '2', '3'],    
    ['4', '5', '6'],    
    ['7', '8', '9'],    
    ['<', '9', 'E'],    
]

# create buttons using `keys`
for y, row in enumerate(keys, 1):
    for x, key in enumerate(row):

        B1 = Button(login, text=key, command=lambda val=key:entry(val))
        B1.grid(row=y, column=x, ipadx=10, ipady=10)
        
login.mainloop()

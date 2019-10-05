    import Tkinter as tk    
    import time  
    import threading  
      
    switch = True  
    root = tk.Tk()  
      
    def blink():  
     def run():  
      while (switch == True):  
       print('BLINK...BLINK...')  
       time.sleep(0.5)  
       if switch == False:  
        break  
     thread = threading.Thread(target=run)  
     thread.start()  
      
    def switchon():    
     global switch  
     switch = True  
     print 'switch on'   
     blink()    
            
    def switchoff():    
     print 'switch off'  
     global switch  
     switch = False      
            
    def kill():    
     root.destroy()    
            
    onbutton = tk.Button(root, text = "Blink ON", command = switchon)    
    onbutton.pack()    
    offbutton =  tk.Button(root, text = "Blink OFF", command = switchoff)    
    offbutton.pack()    
    killbutton = tk.Button(root, text = "EXIT", command = kill)    
    killbutton.pack()    
            
    root.mainloop()  

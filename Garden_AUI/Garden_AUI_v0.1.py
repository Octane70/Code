#Garden_AUI_v0.1
import functools
import os
import random
import time
import commands
import signal
from piui import PiUi

current_dir = os.path.dirname(os.path.abspath(__file__))

#Counter
counter = 0

#time1 = ''

# RPI CPU Temperature
def getTempCPU():
    temp = commands.getoutput("/opt/vc/bin/vcgencmd measure_temp")
    initTempPos = str(temp).find("=")
    finishTempPos = str(temp).find("'")
    temp = str(temp)[initTempPos+1:finishTempPos]
    try:
        temp_num = float(temp)
        return temp_num
    except:
        print "Unable to transform to float"

class DemoPiUi(object):

    def __init__(self):
        self.title = None
        self.txt = None
        self.img = None
        self.ui = PiUi(img_dir=os.path.join(current_dir, 'imgs'))
        self.bttn1 = "Auto"
        self.bttn2 = "Auto"
        self.bttn3 = "Auto"
        self.bttn4 = "Auto"

    def main_menu(self):
        self.page = self.ui.new_ui_page(title="Gardenpi_UI")
        self.list = self.page.add_list()
        self.page.add_textbox("&nbsp;")
        self.page.add_textbox("&nbsp;Temperature =", "h3")
        self.page.add_textbox("&nbsp;Humidity =", "h3")
        self.page.add_textbox("&nbsp;Moisture1 =", "h3")
        self.page.add_textbox("&nbsp;Moisture2 =", "h3")
        if counter % 10 == 0:    
           CPUTemp = getTempCPU()
                  
           self.page.add_textbox("&nbsp;CPU Temp =&nbsp;"+"%0.1fC" % CPUTemp, "h3")
           print CPUTemp 
        time.sleep(1)
        self.page.add_textbox("&nbsp;Case Temp =", "h3")
        self.page.add_element("hr")
        self.page.add_textbox("&nbsp;Watering Times:", "h2")
        self.page.add_textbox("&nbsp;Zone1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +
                              "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Manual", "h2")
        self.frame1 = self.page.add_frame("&nbsp;").backgroundColor= "#ffff00"
        
        self.button1 = self.page.add_button("Auto", self.b1_on_off_auto)
        self.page.add_textbox("&nbsp;")
        self.page.add_textbox("&nbsp;Zone2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + 
                              "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Manual", "h2")
        self.frame2 = self.page.add_frame_black("&nbsp;")
        self.button2 = self.page.add_button("Auto", self.b2_on_off_auto)
        self.page.add_element("hr")
        self.page.add_textbox("&nbsp;Cooling:", "h2")
        self.page.add_textbox("&nbsp;G/H Fan&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +
                              "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Manual", "h2")
        self.frame3 = self.page.add_frame_red("&nbsp;")
        self.button3 = self.page.add_button("Auto", self.b3_on_off_auto)
        self.page.add_textbox("&nbsp;")
        self.page.add_textbox("&nbsp;Case Fan&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + 
                              "&nbsp;&nbsp;&nbsp;Manual", "h2")
        self.frame4 = self.page.add_frame_yellow("&nbsp;")
        self.button4 = self.page.add_button("Auto", self.b4_on_off_auto)
        self.page.add_element("hr")
        self.page.add_textbox("&nbsp;Red = On&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +
                              "&nbsp;&nbsp;&nbsp;&nbsp;Yellow = Auto", "h3")
        self.page.add_textbox("&nbsp;Black = Off", "h3")
        #time.sleep(2)
        self.ui.done()


    def main(self):
        self.main_menu()
        self.ui.done()
        
    #Zone 1
    def b1_on_off_auto(self):
        if self.bttn1 == "Auto":
            self.button1.set_text("Off")
            self.bttn1 = "Off"
            self.frame2
            print "Zone1 Off"
        elif self.bttn1 == "Off":
            self.button1.set_text("On")
            self.bttn1 = "On"
            print "Zone1 On"
        else:
             self.button1.set_text("Auto")
             self.bttn1 = "Auto"
             print "Zone1 Auto"
             
    #Zone 2    
    def b2_on_off_auto(self):
        if self.bttn2 == "Auto":
            self.button2.set_text("Off")
            self.bttn2 = "Off"
            print "Zone2 Off"
        elif self.bttn2 == "Off":
            self.button2.set_text("On")
            self.bttn2 = "On"
            print "Zone2 On"
        else:
             self.button2.set_text("Auto")
             self.bttn2 = "Auto"
             print "Zone2 Auto"
             
    #G/H Fan   
    def b3_on_off_auto(self):
        if self.bttn3 == "Auto":
            self.button3.set_text("Off")
            self.bttn3 = "Off"
            print "G/H Fan Off"
        elif self.bttn3 == "Off":
            self.button3.set_text("On")
            self.bttn3 = "On"
            print "G/H Fan On"
        else:
             self.button3.set_text("Auto")
             self.bttn3 = "Auto"
             print "G/H Fan Auto"
             
    #Case Fan
    def b4_on_off_auto(self):
        if self.bttn4 == "Auto":
            self.button4.set_text("Off")
            self.bttn4 = "Off"
            print "Case Fan Off"
        elif self.bttn4 == "Off":
            self.button4.set_text("On")
            self.bttn4 = "On"
            print "Case Fan On"
        else:
             self.button4.set_text("Auto")
             self.bttn4 = "Auto"
             print "Case Fan Auto"

   #def updates(self, getTempCPU):
       #global CPUTemp
       #Import CPU Temperature // 10 second refresh rate    
       #if counter % 10 == 0:    
     #   CPUTemp = getTempCPU()
       #time.sleep(1)
        
def main():
  piui = DemoPiUi()
  piui.main()

if __name__ == '__main__':
    main()        

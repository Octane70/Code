#Garden_AUI_v0.1
import functools
import os
import random
import time
from piui import PiUi

current_dir = os.path.dirname(os.path.abspath(__file__))

class DemoPiUi(object):

    def __init__(self):
        self.title = None
        self.txt = None
        self.img = None
        self.ui = PiUi(img_dir=os.path.join(current_dir, 'imgs'))
        self.src = "sunset.png"

    def main_menu(self):
        self.page = self.ui.new_ui_page(title="Gardenpi_UI")
        self.list = self.page.add_list()
        self.page.add_textbox("&nbsp;")
        self.page.add_textbox("&nbsp;Temperature =", "h3")
        self.page.add_textbox("&nbsp;Humidity =", "h3")
        self.page.add_textbox("&nbsp;Moisture1 =", "h3")
        self.page.add_textbox("&nbsp;Moisture2 =", "h3")
        self.page.add_textbox("&nbsp;CPU Temp =", "h3")
        self.page.add_textbox("&nbsp;Case Temp =", "h3")
        self.page.add_element("hr")
        self.page.add_textbox("&nbsp;Watering Times:", "h2")
        self.page.add_textbox("&nbsp;Zone1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +
                              "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Manual", "h2")
        frame1 = self.page.add_frame_yellow("&nbsp;", self.ondownclick)
        plus = self.page.add_button("&nbsp;&nbsp;Auto&nbsp;&nbsp;", self.onupclick)
        self.page.add_textbox("&nbsp;")
        self.page.add_textbox("&nbsp;Zone2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + 
                              "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Manual", "h2")
        frame2 = self.page.add_frame_black("&nbsp;", self.ondownclick)
        minus = self.page.add_button("&nbsp;&nbsp;Auto&nbsp;&nbsp;", self.ondownclick)
        self.page.add_element("hr")
        self.page.add_textbox("&nbsp;Cooling:", "h2")
        self.page.add_textbox("&nbsp;G/H Fan&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +
                              "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Manual", "h2")
        frame3 = self.page.add_frame_red("&nbsp;", self.ondownclick)
        plus = self.page.add_button("&nbsp;&nbsp;Auto&nbsp;&nbsp;", self.onupclick)
        self.page.add_textbox("&nbsp;")
        self.page.add_textbox("&nbsp;Case Fan&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + 
                              "&nbsp;&nbsp;&nbsp;Manual", "h2")
        frame4 = self.page.add_frame_yellow("&nbsp;", self.ondownclick)
        minus = self.page.add_button("&nbsp;&nbsp;Auto&nbsp;&nbsp;", self.ondownclick)
        self.page.add_element("hr")
        self.page.add_textbox("&nbsp;Red = On&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +
                              "&nbsp;&nbsp;&nbsp;&nbsp;Yellow = Auto", "h3")
        self.page.add_textbox("&nbsp;Black = Off", "h3")
        self.ui.done()


    def main(self):
        self.main_menu()
        self.ui.done()

    
    def onupclick(self):
        self.title.set_text("Up ")
        print "Up"

    def ondownclick(self):
        self.title.set_text("Down")
        print "Down"    
        
def main():
  piui = DemoPiUi()
  piui.main()

if __name__ == '__main__':
    main()        

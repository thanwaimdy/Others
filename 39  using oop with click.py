# tkinter run with OOP and click
#using CLICK

from tkinter import *

class Appli(Frame):  # built Frame of Appli
    def __init__ (self , x):  # passing through a variable
        Frame.__init__(self , x)
        self.grid()
        self.button_click = 0    # run after click button
        self.create_widget()
        
    def create_widget(self):
        self.button = Button(self)
        self.button['text'] = ("total count : 0 ")
         # here does not do the button
        self.button['command'] = self.cout_click
        self.button.grid()
        
    def cout_click(self):
        self.button_click += 1
        self.button['text'] = ("total click is : ") + str(self.button_click)
                                                      # here str is str data type
               
foot = Tk()
foot.title("72Coder.com")
foot.geometry("400x400")
appli = Appli(foot)  # foot is Tk function is put in the Appli's class.  

foot.mainloop()
        
        
            
                    
    
       
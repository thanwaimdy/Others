# tkinter run with OOP

from tkinter import *

class Appli(Frame):  # built Frame of Appli
    def __init__ (self , x):  # passing through a variable
        Frame.__init__(self , x)
        self.grid()
        self.create_widget()
        
    def create_widget(self):
        self.button1 = Button(self , text("HTLML lessons")
        self.button1.grid()
       
        self.button2 = Button(self)
        self.button2.grid()
        self.button2.configure(text = "CSS lesson")
       
        self.button3 = Button(self)
        self.button3.grid()
        self.button3["text"] = ("JavaScrit lessons")
        
         
foot = Tk()
foot.title("72Coder.com")
foot.geometry("400x400")
appli = Appli(foot)  # foot is Tk function is put in the Appli's class.  

foot.mainloop()
        
        
            
                    
    
       
# message box 

from tkinter import *
	
class Appli(Frame):
    def Frame.__init__(self , x):
        self.grid()
        self.create_widget()
        
    def create_widget(self):
       
        self.text = Text(self, width=35 ,height=5 , wrap=WORD)
        self.text.grid(row=0 ,column=0 ,columnspan=2 ,sticky=W)
        
        self.input = Entry(self)
        self.input.grid(row=1 ,column=0 ,sticky=W)
      
        self.button = Button(self.text = "Clock Me", common = self.waifer_kolar)  
        self.button.grid()
 #here waifer_kolar is mothed to be done will use def

    def waifer_kolar(self):        
        #  print("Hello Burmese Developer")
        message = self.input.get()  
        # message box / took the value in the input with get method 
        self.text.delete(0 ,0 ,END)  # old msg delete and new msg insert.
        self.text.insert(0 ,0 ,message)
        
        
       
          
        
root = Tk()
root.title("72CODER")
root.geometry("250x50")

app =Appli(root)



root.mainloop()


        









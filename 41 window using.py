

from tkinter import *

class Appki(Frame):
    def __init__(self, kolar):
        Frame.__init__(self ,kolar)
        self.grid()
        self.create_widget()
        
    def self.create_widget()  #method
        Label(self.
             	text="Choose any subject you like")
             	.grid(row=0 ,column=0 ,sticky=W)
        	
        Label(self.
             	text="You must choose at lease one")
            	.grid(row=0 ,column=0 ,sticky=W)
        	
    self.php = Boolean Var()   #true or fault
    Checkbutton(self.
    	          text="PHP" ,
    	          variable=self.php ,
    	          command=self.update_text   # to be done 
    	          ).grid(row=2 ,column=0 ,sticky=W)
    
    self.java = Boolean Var()
    Checkbutton(self.
    	          text="JAVA" ,
    	          variable=self.java ,
    	          command=self.update_text   # to be done 
    	          ).grid(row=3 ,column=0 ,sticky=W)
	          
    self.python = Boolean Var()
    Checkbutton(self.
    	          text="Python" ,
    	          variable=self.php ,
    	          command=self.update_text   # to be done 
    	          ).grid(row=4 ,column=0 ,sticky=W)

    self.result = Text(self.width=40 ,heigh=5 ,wrap=WORD)
    self.result.grid(row=5 ,column=0 ,columnspan=3)
    
    def update_text(self):
        
       
      # print("How are you?")  
  # here all buttons are show how are you.
  # so want to show other are following.
         
        like = ""
        if self.php.get():
            like += "You like PHP"
            
        if self.java.get():
            like += "You like JAVA"
            
        if self.python.get():
            like += "You like Python"
            
        self.result.delete(0.0 ,END)
        self.result.insert(0.0 ,like)
            
  	
root = Tk()
root.title("72CODER")
root.geometry("250x250")  # can change
app = Appli(root)
root.mainloop()

        

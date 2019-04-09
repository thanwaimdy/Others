# 42 Menu setting
# final lession of waifer kolar

from tkinter import*

root = Tk()
root.title("72CODER")
root.geometry("300x250")

def call():
    print("Please don't click me")


# creat menu

menu = Menu(root)
root.config(menu=menu)  # config method is no need frame and graid
 
filemenu = Menu(menu.tearoff=0)   # tearoff is off the ----- line , normal is 1 = on
menu.add_cascade(label="File" , menu=filemenu)

filemenu.add_command(label="New" ,command=call ) # if click New call finction will be show.
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")

Myanmarmenu = Menu(menu.tearoff=0)   # tearoff is off the ----- line , normal is 1 = on
menu.add_cascade(label="Myanmar" ,menu=Myanmarmenu)

Myanmarmenu.add_command(label="Developer")
Myanmarmenu.add_command(label="Programmer")
Myanmarmenu.add_command(label="Designer")

Myanmarmenu.add_separator()  # separate and bar show

Myanmarmenu.add_command(label="Gammer")






root.mainloop()


#37 Button and Label

# Tkinter = python2
# tkinter = python3

from Tkinter import *
	
win = Tk()

win.title("Shwethwar")

win.geometry("400x400")

appli = Frame(win)   # Frame to made label and button. # (win)  to fo in the win.
appli.grip()

lab = Label(appli , text("Video lessons")) # here this step nothing to show # need grip. 
lab.grip()   # making the grip lines

bobby = Label(appli , text("PDF lessons"))
bobby.grip()

button1 = Button(appli , text("HTML lessons")
button1.grip()

button2 = Button(appli)
button2.grip()
button2.configure(text="CSS lessons")

button3 = Button(appli)
button3.grip()
button3["text"] = "PHP lessons"


	



win.mainloop()   













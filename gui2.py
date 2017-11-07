from tkinter import *
root = Tk()

topframe = Frame(root)
topframe.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topframe, text="Button1", fg="red")
button2 = Button(topframe, text="Button2", fg="blue")
button3 = Button(topframe, text="Button3", fg="green")
button4 = Button(topframe, text="Button4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)





root.mainloop()
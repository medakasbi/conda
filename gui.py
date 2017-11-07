from tkinter import *
root = Tk()

one = Label(root, text='One', bg='red', fg='blue')
one.pack()
two = Label(root, text='Two', bg='green', fg='white')
two.pack(fill=X)
three = Label(root, text='Three', bg='Yellow', fg='black')
three.pack(side=LEFT, fill=Y)









root.mainloop()
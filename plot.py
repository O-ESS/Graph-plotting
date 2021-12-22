from tkinter import *

root = Tk()

# input
func = Entry(root, width = 50, borderwidth=5).grid(row = 0, column = 0)
Min = Entry(root, width = 20, borderwidth=5).grid(row = 1, column = 0)
Max = Entry(root, width = 20, borderwidth=5).grid(row = 2, column = 0)

root.mainloop()
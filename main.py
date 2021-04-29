import tkinter as tk
from tkinter import *


root = tk.Tk()

canvas = tk.Canvas(root, width= 450, height=550)

#Property size
L1 = tk.Label(root, text= 'Insert the property size')
L1.grid(row=0,column=0)

property_size = tk.Entry(root, bd =4)
property_size.grid(row=0,column=1)

#coordinates


#Exit button
exit_button = tk.Button(root, text="Exit", fg="red", command=root.destroy)
exit_button.grid(row=1,column=1)

root.mainloop()
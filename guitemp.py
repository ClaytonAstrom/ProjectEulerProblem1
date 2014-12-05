from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Multiple of Sums")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Summation of Multiples Calculator").grid(column=1, row=1, columnspan=3)
ttk.Label(mainframe, text="First number").grid(column=1, row=2)
ttk.Label(mainframe, text="Second number").grid(column=3, row=2)
ttk.Label(mainframe, text="Range").grid(column=2, row=3)
firstEnt = ttk.Entry(mainframe).grid(column=1, row=3, sticky=(W, E))
secEnt = ttk.Entry(mainframe).grid(column=3, row=3, sticky=(W, E))
rangeEnt = ttk.Entry(mainframe).grid(column=2, row=4, sticky=(W, E))
ttk.Button(mainframe, text="Calculate!").grid(column=2, row=5, sticky=(W, E))
outResult = ttk.Label(mainframe).grid(column=1, row=6, columnspan=3, rowspan=3)

root.mainloop()
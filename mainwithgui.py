import numbers
from tkinter import *
from tkinter import ttk

debugging = True

#isInt checks that the given input n is an integer. If not, it appends an error message to the log
def isInt(n, log):
	if not isinstance(n, numbers.Integral):
		log = log + "\nInput %d is not an integer!" % n
	return log
		
#isMoreThanOne checks that the given input n is not 1, 0, or negative, to ensure the math runs correctly. If it is, it appends an error message to the log
def isMoreThanOne(n, log):
	if n <= 1:
		log = log + "\nInput %d must be greater than 1!" % n
	return log

#isMult checks if one integer n2 is a multiple of n1, if so, it appends an error message to the log
def isMult(n1, n2, log):
	if (n1 % n2) == 0:
		log = log + "\nInput %d can't be a multiple of %d!" % (n2, n1)
	return log

#isRangeHighest checks that the given input n is not larger than the range, if so, it appends an error message to the log
def isRangeHighest(n, range, log):
	if range <= n:
		log = log + "\nInput %d is larger than the range! %d must be the largest integer." % (n, range)
	return log
		
def calculate(*args):
	baseLog = "The following issues were found: "
	errorLog = baseLog
	errorLog = isInt((num1.get()), errorLog)
	errorLog = isMoreThanOne((num1.get()), errorLog)
	errorLog = isInt((num2.get()), errorLog)
	errorLog = isMoreThanOne((num2.get()), errorLog)
	errorLog = isMult ((num1.get()), (num2.get()), errorLog)
	errorLog = isMult ((num2.get()), (num1.get()), errorLog)

	errorLog = isInt((maxRng.get()), errorLog)
	errorLog = isRangeHighest((num1.get()), (maxRng.get()), errorLog)
	errorLog = isRangeHighest((num2.get()), (maxRng.get()), errorLog)
	
	if errorLog == baseLog:
		'''label displays answer'''
		result.set(1)
	else:
		'''new window opens listing errors'''
		result.set(0)
		print(errorLog)
 
	
	
root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
	
num1 = StringVar()
num2 = StringVar()
maxRng = StringVar()
result = StringVar()

num1_entry = ttk.Entry(mainframe, width=7, textvariable=num1)
num1_entry.grid(column=2, row=1, sticky=(W, E))

num2_entry = ttk.Entry(mainframe, width=7, textvariable=num2)
num2_entry.grid(column=4, row=1, sticky=(W, E))

maxRng_entry = ttk.Entry(mainframe, width=7, textvariable=maxRng)
maxRng_entry.grid(column=3, row=2, sticky=(W, E))

'''testing this'''
ttk.Label(mainframe, textvariable=result).grid(column=2, row=4, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=2, row=3, sticky=W)	

ttk.Label(mainframe, text="First Integer").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Second Integer").grid(column=3, row=1, sticky=E)
ttk.Label(mainframe, text="Range").grid(column=2, row=2, sticky=E)
ttk.Label(mainframe, text="Result").grid(column=1, row=4, sticky=E)
	
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)	

num1_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()

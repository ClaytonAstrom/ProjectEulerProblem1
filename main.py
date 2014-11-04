import numbers

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
		
	
#The program first takes 3 inputs, two integers and a max range. In order to do the math, these inputs must pass certain conditions. If they fail, the user is prompted for inputs again. 
doLoop = True;
while doLoop:
	baseLog = "The following issues were found: "
	errorLog = baseLog
	num1 = input("Input the first integer: ")
	errorLog = isInt(num1, errorLog)
	errorLog = isMoreThanOne(num1, errorLog)
	num2 = input("Input the second integer: ")
	errorLog = isInt(num2, errorLog)
	errorLog = isMoreThanOne(num2, errorLog)
	
	errorLog = isMult (num1, num2, errorLog)
	errorLog = isMult (num2, num1, errorLog)
	
	maxRng = input("Input the range: ")
	errorLog = isInt(maxRng, errorLog)
	errorLog = isRangeHighest(num1, maxRng, errorLog)
	errorLog = isRangeHighest(num2, maxRng, errorLog)
	
	if errorLog == baseLog:
		doLoop = False
	else:
		print(errorLog)
	
	

if debugging:
	print(num1)
	print(num2)
	print(maxRng)




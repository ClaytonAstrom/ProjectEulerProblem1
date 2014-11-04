'''
INPUT:
	sumSeries takes two integers, a number (num) and the highest number we care about (lastNum)


MATH:
	The arithmetic operation for the sum of multiples in a series is: 
	Sn = (n/2) * (a1 + an)
	Sn = sum
	an = highest multiple (highMult)
	n = highMult/num
	a1 = num

OUTPUT:
	sumSeries returns sum
'''
def sumSeries(num, lastNum):
	highMult = lastNum - (lastNum % num)
	sum = ((highMult / num) / 2) * (num + highMult)
	return sum
	

	
'''
This code executes if arithmetic.py is run directly
'''
if __name__ == '__main__':
	num1 = 3
	num2 = 5
	lessThanNum = 1000
	
	lessThanNum = lessThanNum - 1
	
	sumTotal = sumSeries(num1, lessThanNum) + sumSeries(num2, lessThanNum) - sumSeries(num1 * num2, lessThanNum)
	
	print(sumTotal)
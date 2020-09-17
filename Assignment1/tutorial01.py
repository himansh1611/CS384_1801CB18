# Function to add two numbers 
def add(num1, num2): 
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
	multiplication=num1*num2 
	return multiplication

# Function to divide two numbers 
def divide(num1, num2): 
	if num2==0:
		return "Invalid Input"
	else:
		division=num1/num2
		return division


# Function to add power function
# You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2):# num1 ^ num2
	x=isinstance(num1,float) or isinstance(num1,int)
	y=isinstance(num2,float) or isinstance(num2,int)
	if x and y:
		power=1
		if num1==0 and num2==0:
			power=0
		else:
			for i in range(1,int(num2)+1):
				power=num1*power
		
		return power
	else:
		power=0
		return power

# Python 3 program to print GP.  geometric Progression
# You cant use the inbuilt python function. Write your own function
def printGP(a, r, n):
	gp = []
	x = isinstance(a, float) or isinstance(a, int)
	y = isinstance(r, float) or isinstance(r, int)
	z = isinstance(n, float) or isinstance(n, int)
	if x and y and z:
		if r == 0 and n == 1:
			return 0
		else:
			if n >= 1:
				gp.append(a)
				for i in range(1, int(n)):
					a = a * r
					gp.append(a)
				return gp
			if n <= 0:
				gp.append(0)
				return gp
	else:
		gp.append(0)
		return gp
	

# Python 3 program to print AP.  arithmetic Progression
# You cant use the inbuilt python function. Write your own function
def printAP(a, d, n):
	ap = []
	x = isinstance(a, float) or isinstance(a, int)
	y = isinstance(d, float) or isinstance(d, int)
	z = isinstance(n, float) or isinstance(n, int)
	if x and y and z:
		if n>=1:
			ap.append(a)
			for i in range(1, int(n)):
				a += d
				ap.append(a)
			return ap
		if n<=0:
			ap.append(0)
			return ap
	else:
		ap.append(0)
		return ap
	

# Python 3 program to print HP.   Harmonic Progression
# You cant use the inbuilt python function. Write your own function
def printHP(a, d, n):
	
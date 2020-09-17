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
	

# Python 3 program to print AP.  arithmetic Progression
# You cant use the inbuilt python function. Write your own function
def printAP(a, d, n):
	

# Python 3 program to print HP.   Harmonic Progression
# You cant use the inbuilt python function. Write your own function
def printHP(a, d, n):
	
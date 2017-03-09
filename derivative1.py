#this program finds the derivative of f(x) = x^2
#however it can be modified to find the derivative of any function.

def f(x):
	return x**2

def derivative(x):
	#h is the change in x also sometimes called deltaX 
	h = 1./1000.
	#now we just find the slope at point x on our functions curve (that's what derivitives are)
	#slope = rise/run
	rise = f(x + h) - f(x)
	run = h
	slope = rise/run
	print(slope)
	return slope

action = float(raw_input("To find the derivative for f(x) = x^2. Please enter the value of x here> "))

derivative(action)


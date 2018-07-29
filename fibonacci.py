# Write a function, fibonacciFinderN, that will find the nth number in the Fibonacci Sequence.

def fibonacciFinderN(n):
	a = 0
	b = 1
	for j in range(2,n):
		c = a + b
		a = b
		b = c
	return c

# Write fibonacciFinderN as efficiently as possible.

def fibonacciFinderN(n):
	phi = (1 + 5**0.5)*0.5
	return int(round(phi**n/5**0.5))

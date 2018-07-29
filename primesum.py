# Write a function that finds the sum of all prime factors of a given number, n.

def sumFactors(n):
	s = 0
	f = 2
	while n > 1:
		if n%f == 0:
			s += f
			n /= f
		else:
			f += 1
	return s

# Write a function that finds the sum of each unique prime factor of a given number, n. For example, 3 is the only prime factor of 9.

def sumUniqueFactors(n):
	s = 0
	f = 2
	while n > 1:
		if n%f == 0:
			s += f
			while n%f == 0:
				n /= f
		else:
			f += 1
	return s

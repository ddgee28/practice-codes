# Write a function, semiPrimeDetector, that tests if a number, n is a semi-prime number.

def semiPrimeDetector(n):
	m = int(n**0.5)
	count = 0
	for j in range(2,m+1):
		if n%j == 0 and not(n == j**3):
			count += 1
			if count > 1:
				break
	if count == 1:
		return True
	else:
		return False

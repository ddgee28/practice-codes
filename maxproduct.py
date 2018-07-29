# Given an array of integers, write a function, maxProductFinderK, that can be obtained from any k integers in the array.

def maxProductFinderK(A,k):
	Ap = filter(lambda x: x>0, A)
	Am = filter(lambda x: x<=0, A)
	Ap.sort()
	Am.sort()
	Prod = 1
	if len(Ap) == 0:
		if len(Am) >= k:
			for j in range(k):
				Prod *= Am[-1-j]
		else:
			Prod = NaN
	if k%2 == 1:
		Prod *= Ap[-1]
		del Ap[-1]
		k -= 1
	for j in range(int(0.5*k)):
		p1 = Ap[-1]*Ap[-2]
		p2 = Am[0]*Am[1]
		if p1 >= p2:
			Prod *= p1
			del Ap[-1]
			del Ap[-1]
		else:
			Prod *= p2
			del Am[1]
			del Am[1]
	return Prod

# Write a function, productOfTheOthers that, when given an array of n integers, replaces each number in the array with the product of all the numbers in the array except the number itself.

def productOfTheOthers(A):
	n = len(A)
	prodA = 1
	for j in range(n):
		prodA *= A[j]
	out = [None]*n
	for j in range(n):
		out[j] = prodA/A[j]
	return out

# Solve the basic challenge, but this time do so without using division. Call this new function advProductOfTheOthers.

from math import *
def advProdOfTheOthers(A):
	n = len(A)
	depth = int(ceil(log(n,2)))
	tree = [None]*depth
	tree[0] = A
	nj = j
	for j in range(1,depth):
		nj = int(ceil(nj*0.5))
		tree[j] = [None]*nj
		if len(tree[j-1])%2 == 0:
			for k in range(nj):
				tree[j][k] = tree[j-1][2*k-1] * tree[j-1][2*k]
		else:
			for k in range(dn-1):
				tree[j][k] = tree[j-1][2*k-1] * tree[j-1][2*k]
			tree[j][nj] = tree[j-1][-1]
	out = [None]*n
	for m in range(n):
		prod = 1
		mj = m
		for j in range(1,depth):
			if mj == len(tree[j-1]) and mj%2 == 1:
				mj = int(0.5*mj+0.5)
			elif mj%2 == 0:
				prod *= tree[j-1][mj-1]
				mj = int(0.5*mj)
			else:
				prod *= tree[j-1][mj+1]
				mj = int(0.5*mj+0.5)
		out[m] = prod
	return out

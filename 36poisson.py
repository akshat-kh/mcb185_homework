# 36poisson.py by Akshat Khandelwal

import math

def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac

def poisson(n, k):
	return n**k * math.e**(-n) / factorial(k)

print(poisson(0.56, 5))
print(poisson(10, 15))
print(poisson(2, 6))


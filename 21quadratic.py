# 21quadratic.py by Akshat Khandelwal

import math
import sys

"""
Function to implement the quadratic formula
Coefficients a, b, and c are passed through
Returns 0,1, or 2 x-intercepts depending on 
the values
""" 
def quad_formula(a, b, c):
	d = b**2 - 4 * a * c  # Calculating discriminant value
	if d < 0:
		sys.exit("No possible solution: can't square root a negative number")
	elif d == 0:
		x = -b / (2 * a)
		return x
	else:
		x1 = (math.sqrt(d) - b) / (2 * a)
		x2 = (math.sqrt(d) + b) / (2 * a)
		return x1, x2

# Test cases
print(quad_formula(1, -4, 4))
print(quad_formula(1, 2, -3))
print(quad_formula(1, 1, 2))


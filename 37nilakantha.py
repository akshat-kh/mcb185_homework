# 37nilakantha.py

import math

pi = 3
for n in range(2, 100, 2):
	if n % 4 == 0:
		pi = pi - (4 / (n * (n + 1) * (n + 2)))
	else:
		pi = pi + (4 / (n * (n + 1) * (n + 2)))
	print(pi)


# 44randompi.py by Akshat Khandelwal

import math
import random

total = 0
inside = 0
while True:
	total += 1
	x = random.random()
	y = random.random()
	dist =  math.sqrt(x**2 + y**2)
	if dist > 0 and dist <= 1: 
		inside += 1
	print(4 * inside / total)

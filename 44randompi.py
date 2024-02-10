# 44randompi.py by Akshat Khandelwal

import math
import random

total = 0
inside = 0
while 1 == 1:
	total += 1
	x = random.gauss(0.0, 1.0)
	y = random.gauss(0.0, 1.0)
	dist =  math.sqrt(x**2 + y**2)
	if dist < 1:
		inside += 1
	print(inside / total)

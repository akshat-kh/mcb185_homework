# 33triples by Akshat Khandelwal

import math 

def is_perfect_square(n):
	root = math.sqrt(n)
	if math.isclose(root, root // 1): return True
	return False

for a in range(1, 100):
	for b in range(a + 1, 100):
		c_squared = a**2 + b**2
		if is_perfect_square(c_squared):
			print(a, b, math.sqrt(c_squared))


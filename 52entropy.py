# 52entropy.py by Akshat Khandelwal

import sys
import math

prob_dist = []
for arg in sys.argv[1:]:
	num = float(arg)
	assert(num > 0 and num < 1)
	prob_dist.append(num)

sum = 0
for prob in prob_dist:
	sum += prob
if not math.isclose(sum, 1.0):
	sys.exit('Error: probs dont add up to 1.')

ent = 0
for prob in prob_dist:
	ent -= prob * math.log2(prob)

print(ent)

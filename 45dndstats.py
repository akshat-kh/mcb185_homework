# 45dndstats.py by Akshat Khandelwal

import random
import math

rolls = 100

# 3D6 rule
sum_3d6 = 0
for i in range(rolls):
	roll_score = 0
	for j in range(3):
		roll_score += random.randint(1, 6)
	sum_3d6 += roll_score
print('3D6 average: ', sum_3d6 / rolls)

# 3D6r1 rule
sum_3d6r1 = 0
for i in range(rolls):
	roll_score = 0
	for j in range(3):
		roll = random.randint(1, 6)
		if roll == 1:
			roll = random.randint(1, 6)
		roll_score += roll
	sum_3d6r1 += roll_score
print('3D6R1 average: ', sum_3d6r1 / rolls)

# 3D6x2 rule
sum_3d6x2 = 0
for i in range(rolls):
	roll_sum = 0
	for j in range(3):
		r1 = random.randint(1, 6)
		r2 = random.randint(1, 6)
		if r1 > r2:
			roll_sum += r1
		else:
			roll_sum += r2
	sum_3d6x2 += roll_sum
print('3D6x2 average: ', sum_3d6x2 / rolls)

# 4D6d1 rule
sum_4d6d1 = 0
for i in range(rolls):
	roll_sum = 0
	r1 = random.randint(1, 6)
	r2 = random.randint(1, 6)
	r3 = random.randint(1, 6)
	r4 = random.randint(1, 6)
	if r1 < r2 and r1 < r3 and r1 < r4:
		roll_sum += r2 + r3 + r4
	elif r2 < r1 and r2 < r3 and r2 < r4:
		roll_sum += r1 + r3 + r4
	elif r3 < r1 and r3 < r2 and r3 < r4:
		roll_sum += r1 + r2 + r4
	else:
		roll_sum += r1 + r2 + r3
	sum_4d6d1 += roll_sum
print('4D6d1 average: ', sum_4d6d1 / rolls)

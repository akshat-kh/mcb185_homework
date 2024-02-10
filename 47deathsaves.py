# 47deathsaves.py by Akshat Khandelwal

import random

wins = 0
fails = 0
revives = 0
deaths = 0
stable = 0
rolls = 10
for i in range(rolls):
	roll = random.randint(1, 20)
	if roll == 1:
		fails += 2
	elif roll != 1 and roll < 10:
		fails += 1
	elif roll >= 10 and roll != 20:
		wins += 1
	else:
		revives += 1
	if wins == 3:
		stable += 1
	if fails == 3:
		deaths += 1
print('die: ', deaths / rolls)
print('stabilize: ', stable / rolls)
print('revive: ', revives / rolls)

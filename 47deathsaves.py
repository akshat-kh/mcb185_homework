# 47deathsaves.py by Akshat Khandelwal

import random


revives = 0
deaths = 0
stable = 0
rolls = 10000
for i in range(rolls):
	wins = 0
	fails = 0
	while True:
		roll = random.randint(1, 20)
		if roll == 1:
			fails += 2
		elif roll == 20:
			revives += 1
			break
		elif roll != 1 and roll < 10:
			fails += 1
		else:
			wins += 1
			
		if wins == 3:
			stable += 1
			break
			
		if fails >= 3:
			deaths += 1
			break
			
print('die: ', deaths / rolls)
print('stabilize: ', stable / rolls)
print('revive: ', revives / rolls)

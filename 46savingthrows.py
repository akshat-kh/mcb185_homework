# 46savingthrows.py by Akshat Khandelwal

import random

def normal_roll():
	return random.randint(1, 20)

def advantage_roll():
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20)
	if roll1 > roll2:
		return roll1
	else:
		return roll2
def disadvantage_roll():
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20)
	if roll1 < roll2:
		return roll1
	else:
		return roll2

print('DC', end='\t') 
print('Normal roll', end='\t')
print('Adv roll', end='\t')
print('Disadv roll')
print('----------------------------------------------------')
rolls = 20
for dc in range(5, 20, 5):
	print(dc, end='\t')
	normal_wins = 0
	normal_total = 0
	for i in range(rolls):
		normal_total += 1
		roll = normal_roll()
		if roll >= dc:
			normal_wins += 1
	print(normal_wins / normal_total, end='\t')
	print(end='\t')
	adv_wins = 0
	adv_total = 0
	for j in range(rolls):
		adv_total += 1
		roll = advantage_roll()
		if roll >= dc:
			adv_wins += 1
	print(adv_wins / adv_total, end='\t')
	print(end='\t')
	dis_wins = 0
	dis_total = 0
	for k in range(rolls):
		dis_total += 1
		roll = disadvantage_roll()
		if roll >= dc:
			dis_wins += 1
	print(dis_wins / dis_total)


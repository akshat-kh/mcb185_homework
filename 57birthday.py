# 57birthday.py by Akshat Khandelwal

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

# Main loop
collisions = 0
for t in range(trials):
	# Create calendar list
	calendar = []
	for i in range(days):
		calendar.append(0)
		
	# Randomly assigning people to birthdays
	for p in range(people):
		bd = random.randint(1, days)
		calendar[bd - 1] += 1
		
	# Checking for similar birthdays
	shared = False
	calendar.sort()
	if 2 in calendar:
		shared = True
	if shared: collisions += 1
print(collisions / trials)	
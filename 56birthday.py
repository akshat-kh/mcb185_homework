# 56birthday.py by Akshat Khandelwal

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

# Main loop
collisions = 0
for trial in range(trials):
	# Fill up the classroom
	birthdays = []
	for i in range(people):
		day = random.randint(1, days)
		birthdays.append(day)
	
	# Now, we check for similar birthdays
	shared = False
	birthdays.sort()

	for i in range(1, len(birthdays)):
		if birthdays[i - 1] == birthdays[i]:
			shared = True
			break
	if shared: collisions += 1
print(collisions / trials)


	
	

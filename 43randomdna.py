# randomdna.py by Akshat Khandelwal

import random

sequences = 3
for i in range(1, sequences + 1):
	print(f'>seq-{i}')
	seq_len = random.randint(50, 60)
	for j in range(seq_len):
		print(random.choice('ACGT'), end='')
	print()


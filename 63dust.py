# 63dust.py by Akshat Khandelwal

import sys
import mcb185
import math

path = sys.argv[1]
w = int(sys.argv[2])
threshold = float(sys.argv[3])

defline = ''
copy_seq = []

for defline, seq in mcb185.read_fasta(path):
	for nt in seq:
		copy_seq.append(nt)
	
	for i in range(len(seq) - w + 1):
		h = 0
		s = seq[i:i+w]
		
		for nt in 'ACGT':
			p = s.count(nt) / w
			if p > 0:
				h -= p * math.log2(p)
			
		if h < threshold:
			for j in range(i, i + w):
				copy_seq[j] = 'N'
				
copy_seq = ''.join(copy_seq)
print('>', end='')
print(defline)
for i in range(0, len(copy_seq), 60):
	print(copy_seq[i:i+60])

# 62skewer.py by Akshat Khandelwal

import sys
import mcb185
import dogma

path = sys.argv[1]
w = int(sys.argv[2])
g = 0
c = 0
#total_nts = 0
for defline, seq in mcb185.read_fasta(path):
	for i in range(len(seq) - w + 1):
		initial = seq[:w]
		g = initial.count('G')
		c = initial.count('C')
		nt = seq[i]
		s = seq[i:i+w]
		if nt == 'G':
			g -= 1
		elif nt == 'C':
			c -= 1
		
		if s == 'G':
			g += 1
		elif s == 'C':
			c += 1
	
		comp = (g + c) / w
		if g + c == 0:
			skew = 0
		else:
			skew = (g - c) / (g + c)
		print(i, end ='  ')
		print('GC comp: ', comp, end='  ')
		print('GC skew: ', skew)
	
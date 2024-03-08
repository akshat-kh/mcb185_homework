# 63dust.py by Akshat Khandelwal

import sys
import mcb185
import math

path = sys.argv[1]
w = int(sys.argv[2])
threshold = float(sys.argv[3])

a = 0
g = 0
c = 0
t = 0
total_nts = 0
h = 0
defline = ''
print('>', end='')
for defline, seq in mcb185.read_fasta(path):
	print(defline)
	for i in range(len(seq) - w + 1):
		s = seq[i:i+w]
		if i == 0:
			a += s.count('A')
			g += s.count('G')
			c += s.count('C')
			t += s.count('T')
			total_nts += w
		else:
			end_nt = s[len(s) - 1]
			a += end_nt.count('A')
			g += end_nt.count('G')
			c += end_nt.count('C')
			t += end_nt.count('T')
			total_nts += 1
		a_prop = a / total_nts
		c_prop = c / total_nts
		g_prop = g / total_nts
		t_prop = t / total_nts
		h -= (a_prop * math.log2(a_prop)) + (c_prop * math.log2(c_prop)) + (g_prop * math.log2(t_prop)) + (t_prop * math.log2(t_prop))
		if h < threshold:
			for j in range(i, len(s)):
				seq[j] = 'N'
		print(seq[i:i+60)

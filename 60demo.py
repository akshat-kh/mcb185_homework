# 60demo.py by Akshat Khandelwal

import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	nts = 'ACGTN'
	print(name, end='\t')
	for nt in nts:
		print(seq.count(nt) / len(seq), end='\t')
	print()

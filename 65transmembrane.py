# 65transmembrane.py

import sys
import mcb185

def kdh(seq):
	h = 0
	for aa in seq:
		if aa == 'I':
			h += 4.5
		elif aa == 'V':
			h += 4.2
		elif aa == 'L':
			h += 3.8
		elif aa == 'F':
			h += 2.8
		elif aa == 'C':
			h += 2.5
		elif aa == 'M':
			h += 1.9
		elif aa == 'A':
			h += 1.8
		elif aa == 'G':
			h += -0.4
		elif aa == 'T':
			h += -0.7
		elif aa == 'S':
			h += -0.8
		elif aa == 'W':
			h += -0.9
		elif aa == 'Y':
			h += -1.3
		elif aa == 'P':
			h += -1.6
		elif aa == 'H':
			h += -3.2
		elif aa == 'E':
			h += -3.5
		elif aa == 'Q':
			h += -3.5
		elif aa == 'D':
			h += -3.5
		elif aa == 'N':
			h += -3.5
		elif aa == 'K':
			h += -3.9
		elif aa == 'R':
			h += -4.5
	return h / len(seq)
		
def has_region(seq, aa_num, min_hydro):
	for i in range(len(seq) - aa_num + 1):
		pep = seq[i:i+aa_num]
		if kdh(pep) >= min_hydro and 'P' not in pep:
			return True
		return False
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	s1 = seq[0:30]
	s2 = seq[30:]
	if has_region(s1, 8, 2.5) and has_region(s2, 11, 2.0):
		print(defline)	

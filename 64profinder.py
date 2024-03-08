# 64profinder.py by Akshat Khandelwal

import sys
import mcb185
import dogma

path = sys.argv[1]
min_seq_len = int(sys.argv[2])

def proteins(seq, min_len):
	proteins = []
	for win in range(3):
		aas = dogma.translate(seq[win:])
		orfs = aas.split('*')
		for orf in orfs:
			if 'M' not in orf:
				continue
			start = orf.index('M')
			if len(orf[start:]) >= min_len:
				proteins.append(orf[start:])
	return proteins

for defline, seq in mcb185.read_fasta(path):
	defwords = defline.split()
	pcount = 1
	for p1 in proteins(seq, min_seq_len):
		print(f'>{defwords[0]}-prot-{pcount}')
		print(p1)
		pcount += 1					
	for p2 in proteins(dogma.revcomp(seq), min_seq_len):
		print(f'>{defwords[0]}-prot-{pcount}')
		print(p2)
		pcount += 1

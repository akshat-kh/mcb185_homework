# 73missingkmers.py by Akshat Khandelwal

import sys
import mcb185
import dogma
import itertools


k = 0

while True:
	k += 1
	kcount = {}  
	print(k, file=sys.stderr)
	
	for defline, seq in mcb185.read_fasta(sys.argv[1]):	
		
		# Strand 1
		for i in range(len(seq) - k + 1):
			kmer = seq[i:i+k]
			if kmer not in kcount:
				kcount[kmer] = 0
			kcount[kmer] += 1
		
		# Strand 2
		revseq = dogma.revcomp(seq)
		for i in range(len(revseq) - k + 1):
			kmer = revseq[i:i+k]
			if kmer not in kcount:
				kcount[kmer] = 0
			kcount[kmer] += 1
			
	
	if len(kcount.keys()) == 4**k:
		continue				
	missing = False
	for t in itertools.product('ACGT', repeat=k):
		kmer = ''.join(t)
		if kmer not in kcount:
			missing = True
			print(kmer)
	if missing:
		break	
		
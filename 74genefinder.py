# 74genefinder.py

import mcb185
import dogma
import sys

min_orf_len = int(sys.argv[2])
def get_orfs(fseq, reversed):
	i = 0
	orfs = []
	while i < len(seq):
		codon = fseq[i:i+3]
		if codon != 'ATG':
			i += 3
			continue
		start = i
			
		for j in range(i, len(fseq) - 2, 3):
			codon = fseq[j:j+3]
			if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
				stop = j
				if (stop - start) > min_orf_len:
					if reversed:
						orfs.append([len(fseq)-i-1-frame, len(fseq)-j-1-frame])
					else:
						orfs.append([i+1+frame, j+3+frame])
				i = j
				break
		i += 3
	return orfs

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	rev = dogma.revcomp(seq)
	for frame in range(3):
# 		print('frame ', frame)
		fseq = seq[frame:]
		rfseq = rev[frame:]
		# print('+ strand: ', get_orfs(fseq, False))
# 		print()
# 		print('- strand: ', get_orfs(rfseq, True))
		forward_coords = get_orfs(fseq, False)
		rev_coords = get_orfs(rfseq, True)
		
		for i in range(len(forward_coords)):
			print(f'NC_00913.{i}', end='\t')
			print('RefSeq', end='\t')
			print('CDS', end='\t')
			print(forward_coords[i][0], end='\t')
			print(forward_coords[i][1], end='\t')
			print('.', end='\t')
			print('+', end='\t')
			print()

		for j in range(len(rev_coords)):
			print(f'NC_00913.{j}', end='\t')
			print('RefSeq', end='\t')
			print('CDS', end='\t')
			print(forward_coords[j][0], end='\t')
			print(forward_coords[j][1], end='\t')
			print('.', end='\t')
			print('-', end='\t')
			print()
			
							
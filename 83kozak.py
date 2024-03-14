# 83kozak.py by Akshat Khandelwal

import sys
import gzip
import dogma

inits = []
genome = []
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		line = line.rstrip()
		if 'CDS' in line and '..' in line:
			if 'join' in line: continue
			elif 'complement' in line:
				s1 = line.index('(')
				s2 = line.index(')')
				s = line[s1+1:s2]
				start, end = s.split('..')
				inits.append((int(start), int(end), 'reverse'))
			else:
				words = line.split()
				start, end = words[1].split('..')
				inits.append((int(start), int(end), 'forward'))
		elif 'ORIGIN' in line:
			for line in fp:
				nts = line.split()
				for nt in nts[1:]:
					genome.append(nt)
			seq = ''.join(genome)
			seq = seq.upper()
kozaks = []
for i in range(14):
	kozaks.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

for start, end, strand in inits:
	if strand == 'forward':
		kplus = seq[start-9:start+5]
		for i, nt in enumerate(kplus):
			kozaks[i][nt] += 1
	elif strand == 'reverse':
		rseq = dogma.revcomp(seq[end-6:end+8])
		for i, nt in enumerate(rseq):
			kozaks[i][nt] += 1
			
print('AC RS001')
print('XX')
print('ID ECKOZ')
print('XX')
print("DE Hi, Dr. Korf")
print(f'{"PO":<8}', f'{"A":<8}', f'{"C":<8}', f'{"G":<8}', f'{"T":<8}')
for i in range(len(kozaks)):
	print(f'{i+1:<8}', f'{kozaks[i]["A"]:<8}', f'{kozaks[i]["C"]:<8}', 
	f'{kozaks[i]["G"]:<8}', f'{kozaks[i]["T"]:<8}')
print('XX')

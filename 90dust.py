#!/usr/bin/env python3
# 90dust.py by Akshat Khandelwal

import mcb185
import argparse
import math

# parser = argparse.ArgumentParser(description='DNA entropy filter.')
# parser.add_argument('file', type=str, help='name of fasta file')
# parser.add_argument('size', type=int, help='window size')
# parser.add_argument('entropy', type=float, help='entropy threshold')
# arg = parser.parse_args()
# print('dusting with', arg.file, arg.size, arg.entropy)
# 
# print('first', 'second')
# print('first', 'second', sep='\t', end='\n')
# print('first', 'second', end='\n', sep='\t')

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
# print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)
copy_seq = []
for defline, seq in mcb185.read_fasta(arg.file):
	for nt in seq:
		copy_seq.append(nt)
	if arg.lower:
		for i in range(len(seq) - arg.size + 1):
			h = 0
			s = seq[i:i+arg.size]
			
			for nt in 'ACGT':
				p = s.count(nt) / arg.size
				if p > 0:
					h -= p * math.log2(p)
				
			if h < arg.entropy:
				for j in range(i, i + arg.size):
					copy_seq[j] = (copy_seq[j].lower())

copy_seq = ''.join(copy_seq)
print('>', end='')
print(defline)
for i in range(0, len(copy_seq), 60):
	print(copy_seq[i:i+60])

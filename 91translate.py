#!/usr/bin/env python3
# 91translate.py by Akshat Khandelwal

import mcb185
import argparse

parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', type=str, help='fasta files of mRNAs')
parser.add_argument('-m', '--min', type=int, default=100,
	help='minimum protein length [%(default)i]')
parser.add_argument('-a', '--anti', action='store_true', 
	help='also examine the anti-parallel strand')
arg = parser.parse_args()
# print('translating with', arg.file, arg.min, arg.anti)

codons = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}
def translate(seq):
	pro_seq = []
	for i in range(0, len(seq), 3):
		codon = seq[i:i+3]
		if codon in codons: 
			aa = codons[codon]
		else:              aa = 'X'	
		if aa == '*':
			break
		pro_seq.append(aa)
	return ''.join(pro_seq)

for defline, seq in mcb185.read_fasta(arg.file):
	start = seq.index('ATG')
	s = seq[start:]
	print('>', end='')
	print(defline)
	print('Forward strand:', translate(s))
	if arg.anti:
		rseq = mcb185.anti_seq(seq)
		rstart = rseq.index('ATG')
		print('Anti strand:', translate(rseq[rstart:]))
	

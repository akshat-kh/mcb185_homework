# 84splicesites.py by Akshat Khandelwal

import sys
import gzip
import mcb185
import dogma
import json

def print_pwm(pwm, acc_num, chr_id, desc):
	print('AC', acc_num)
	print('XX')
	print('ID', chr_id)
	print('XX')
	print('DE', desc)
	print(f'{"PO":<8}', f'{"A":<8}', f'{"C":<8}', f'{"G":<8}', f'{"T":<8}')
	for i in range(len(pwm)):
		print(f'{i+1:<8}', f'{pwm[i]["A"]:<8}', f'{pwm[i]["C"]:<8}', 
		f'{pwm[i]["G"]:<8}', f'{pwm[i]["T"]:<8}')
	print('XX')
	print('//')

chrom = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	chr_id = defline.split()[0]
	chrom[chr_id] = seq


introns = []
with gzip.open(sys.argv[2], 'rt') as fp:
	for line in fp:
		words = line.split('\t')
		ch = words[0]
		feat_type = words[2]
		start = int(words[3]) - 1
		end = int(words[4]) - 1
		num = words[5]
		strand = words[6]
		if feat_type != 'intron': continue
		if num == '.': continue
		else: num = float(num)
		
		introns.append((ch, start, end, num, strand))
donos = []
for i in range(6):
	donos.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

accs = []
for i in range(7):
	accs.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

for ch, start, end, num, strand in introns:
	if strand == '+':
		intron = chrom[ch][start:end+1]
	else:
		#print('forward:', intron)
		intron = mcb185.anti_seq(chrom[ch][start:end+1])
		# print('reverse:', intron)
		
	donor_seq = intron[0:6]
	for i, nt in enumerate(donor_seq):
		donos[i][nt] += 1
		
	acc_seq = intron[-7:]
	for i, nt in enumerate(acc_seq):
		accs[i][nt] += 1

print_pwm(donos, 'IDK001', 'DON', 'Donor site')
print_pwm(accs, 'IDK002', 'ACC', 'Acceptor site')
	

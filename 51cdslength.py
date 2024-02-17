# 51cdslength.py

import gzip

path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#':
			continue
		words = line.split()
		if words[2] != 'CDS':
			continue
		begin = int(words[3])
		end = int(words[4])
		print(end - begin + 1)


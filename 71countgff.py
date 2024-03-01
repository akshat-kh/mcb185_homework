# 71countgff.py by Akshat Khandelwal

import sys
import gzip

count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'):
			continue
		f = line.split()
		feature = f[2]
		if feature not in count:
			count[feature] = 0
		count[feature] += 1
for k in sorted(count):
	print(k, count[k])

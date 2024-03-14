# 82transfac.py by Akshat Khandelwal

import sys
import json
import gzip
import re

catalog = []
with gzip.open(sys.argv[1], 'rt') as fp:
	uid, pwms = None, []
	for line in fp:
		if line.startswith('ID'):
			uid = line[3:len(line)-1]
			
		elif re.search('^\d', line):
			n, a, c, g, t = line.split()
			a = float(a)
			c = float(c)
			g = float(g)
			t = float(t)
			pwms.append({'A': a, 'C': c, 'G': g, 'T': t})
		
		elif line.startswith('XX'):
			record = {'id': uid, 'pwm': pwms}
			if len(pwms) > 0: catalog.append(record)
			pwms = []	

print(json.dumps(catalog, indent=4))

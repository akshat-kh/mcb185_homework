# 55colorname.py by Akshat Khandelwal

import sys

def dtc(X, Y):
	d = 0
	for x, y in zip(X, Y):
		d += abs(x - y)
	return d

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
min_dist = 100000
min_color = ''
fp = open(colorfile)
for line in fp:
	words = line.split()
	r, g, b = words[2].split(',')
	r = int(r)
	g = int(g)
	b = int(b)
	dist = dtc([r, g, b], [R, G, B]) 
	if dist < min_dist:
		min_dist = dist
		min_color = words[0]
print(min_color)
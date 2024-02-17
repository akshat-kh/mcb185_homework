# 53genomestats.py by Akshat Khandelwal

import sys
import gzip

path = sys.argv[1]
feat = sys.argv[2]
feat_lens = []

with gzip.open(path, 'rt') as fp:
	for line in fp:
		words = line.split()
		if words[2] != feat:
			continue
		begin = int(words[3])
		end = int(words[4])
		feat_lens.append(end - begin + 1)	
		
feat_lens.sort()
median = 0
mid = len(feat_lens) // 2
if len(feat_lens) % 2 == 0:
	median = (feat_lens[mid] + feat_lens[mid - 1]) / 2
else:
	median = feat_lens[mid]

sum = 0
for feat_len in feat_lens:
	sum += feat_len
mean = sum / len(feat_lens)

sd = 0
for feat_len in feat_lens:
	sd += (feat_len - mean)**2
sd = (sd / len(feat_lens))**0.5
		
print('Count: ', len(feat_lens))
print('Min: ', feat_lens[0])
print('Max: ', feat_lens[len(feat_lens) - 1])
print('Mean: ', f'{sum / len(feat_lens):.2f}')
print('Standard Deviation: ', f'{sd:.2f}')
print('Median: ', f'{median:.2f}')

# 24accuracy.py by Akshat Khandelwal

import sys

def scores(tp, fp, tn, fn):
	acc = (tp + tn) / (tp + tn + fp + fn)
	f1 = tp / (tp + (0.5 * (fp + fn)))
	return acc, f1

# Test cases
print(scores(25, 25, 25, 25))
print(scores(50, 25, 50, 25))

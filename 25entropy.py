# 25entropy.py by Akshat Khandelwal

import math

def entropy(a, c, g, t):
	if a == 0 or c == 0 or g == 0 or t == 0:
		return
	else:
		# Converting counts to percentages
		a_percent = a / (a + c + g + t)
		c_percent = c / (a + c + g + t)
		g_percent = g / (a + c + g + t)
		t_percent = t / (a + c + g + t)
		
		# Applying Shannon Entropy formula: sum of all P(Xi) * log2(P(Xi))
		a_entropy = a_percent * math.log2(a_percent)
		c_entropy = c_percent * math.log2(c_percent)
		g_entropy = g_percent * math.log2(g_percent)
		t_entropy = t_percent * math.log2(t_percent)

		total_entropy = a_entropy + c_entropy + g_entropy + t_entropy
		return total_entropy

# Test cases
print(entropy(4, 4, 4, 4))
print(entropy(10, 5, 10, 5))
print(entropy(0, 5, 0, 5))

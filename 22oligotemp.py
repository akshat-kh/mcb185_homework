# 22oligotemp.py by Akshat Khandelwal

# Calculates and returns melting temperature of oligo, given ACGT content
def oligo_temp(a, c, g, t):
	oligo = a + c + g + t  # Calculate total length of oligo, using ACGT counts
	if oligo <= 13:
		tm = (a + t) * 2 + (g + c) * 4  # Case 1
	else:
		tm = 64.9 + 41 * (g + c - 16.4) / (a + c + g + t)  # Case 2
	return tm

# Test cases
print(oligo_temp(2, 2, 2, 2))
print(oligo_temp(4, 2, 4, 2))
print(oligo_temp(13, 13, 9, 9))
print(oligo_temp(20, 20, 15, 15))

# 34scoringmatrix by Akshat Khandelwal

bases = 'ACGT'
print('  ', end = ' ')
for base in bases:
	print(base, end = '  ')
print()
for nt1 in bases:
	print(nt1, end = ' ')
	for nt2 in bases:
		if nt1 == nt2:
			print('+1', end = ' ')
		else:
			print('-1', end = ' ')
	print()
	
		

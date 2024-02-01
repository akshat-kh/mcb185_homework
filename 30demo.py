# 30demo.py by Akshat Khandelwal
i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):
	print(i)

for i in range(0, 5):
	print(i)

for i in range(5):
	print(i)

for char in 'hello':
	print(char)

seq = 'GAATTC'
for nt in seq:
	print(nt)

for nt1 in 'ACGT':
	for nt2 in 'ACGT':
		if nt1 == nt2: 
			print(nt1, nt2, '+1')
		else:
			print(nt1, nt2, '-1')

nts = 'ACGT'
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2:
			print(nt1, nt2, '+1')
		else:
			print(nt1, nt2, '-1')

limit = 4
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i+1, j+1)

def gc_comp(seq):
	gc_count = 0
	total = 0
	for nt in seq:
		if nt == 'C' or nt == 'G':
			gc_count = gc_count + 1
		total = total + 1
	return gc_count / total

print(gc_comp('ACAGCGAAT'))

def tri_num(n):
	sum = 0
	for i in range(1, n + 1):
		sum = sum + i
	return sum

print(tri_num(5))
print(tri_num(11))

def factorial(n):
	if n == 0: return 1
	fact = 1
	for i in range(1, n + 1):
		fact = fact * i
	return fact

print(factorial(4))

def euler(limit):
	e = 0
	for i in range(limit):
		e = e + (1 / factorial(i))
	return e

print(euler(4))

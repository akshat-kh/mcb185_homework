# 32fibonacci by Akshat Khandelwal

fib_1 = 0
fib_2 = 1
total = 0
print(fib_1)
print(fib_2)
for i in range(8):
	total = fib_1 + fib_2
	fib_1 = fib_2
	fib_2 = total
	print(fib_2)

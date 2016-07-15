from math import floor, sqrt

def num_divisors(n):
	num_divisors = 0
	max = floor(sqrt(n))
	for i in range(1, max + 1):
		if n % i == 0:	
			num_divisors += 1 if i == max else 2
	return num_divisors

triangular_num = 1
count = 1
while num_divisors(triangular_num) < 500:
	count += 1
	triangular_num = (count ** 2 + count) // 2

print(triangular_num)
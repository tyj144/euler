from math import floor, sqrt
def is_prime(n):
	for num in range(2, floor(sqrt(n)) + 1):
		if n % num == 0: 
			return False
	return True

num_primes = 0
n = 2

while num_primes < 10001: 
	if is_prime(n): num_primes += 1
	if num_primes == 10001: print(n)
	n += 1

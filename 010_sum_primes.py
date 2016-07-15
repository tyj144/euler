from math import floor, sqrt

def is_prime(n):
	if n % 2 == 0:
		if n == 2: return True
		else: return False
	for num in range(3, floor(sqrt(n)) + 1, 2):
		if n % num == 0: 
			return False
	return True
	
print(sum(i for i in range(2, 2000000) if is_prime(i)))
from math import *

def find_largest_prime_factor(n):
	"""
	Goes through each possible factor for n and stores them in a dictionary.
	Then, each factor's primality is tested, and the largest prime factor is
	found.
	"""
	largest_prime_factor = 1
	factors = {}
	for possible_factor in range(2, floor(sqrt(n)) + 1):
		if n % possible_factor == 0:
			factors[possible_factor] = n // possible_factor
			
	for f in factors:
		if is_prime(f) and f > largest_prime_factor:
			largest_prime_factor = f
			
	return largest_prime_factor
				
def is_prime(n):
	"""
	Tests all numbers between 2 and the square root of n to see if there
	are any factors.
	(It would be optimal to only test prime factors, but obviously if I
	knew all the prime factors, I wouldn't need this method in the first 
	place.)
	"""
	for num in range(2, floor(sqrt(n)) + 1):
		if n % num == 0:
			return False
	return True
	
print(find_largest_prime_factor(600851475143))
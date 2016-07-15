# Project Euler's Primality Test
# https://projecteuler.net/overview=007
from math import floor, sqrt

def is_prime(n):
	if n == 1: return False
	elif n < 4: return True
	elif n % 2 == 0: return False
	elif n < 9: return True
	elif n % 3 == 0: return False
	else:
		max_factor = floor(sqrt(n))
		factor = 5
		while factor <= max_factor:
			if n % factor == 0: return False
			if n % (factor + 2) == 0: return False
			factor += 6
		return True
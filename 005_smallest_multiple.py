num = 2 ** 4 * 3 ** 2 * 5 * 7 * 11 * 13 * 17 * 19

def is_multiple(n):
	for i in range(1, 21):
		if n % i != 0:
			return False
	# print("{} is a multiple of all numbers 1 to 20.".format(num))
	return True

# print(is_multiple(num))
print(num)
def is_palindrome(num):
	num = str(num)
	start = 0
	end = len(num) - 1
	while start <= end:
		if num[start] != num[end]:
			return False
		start += 1
		end -= 1
	return True

def has_triple_digit_factors(palindrome):
	for factor in range(100, 999):
		if palindrome % factor == 0 and len(str(palindrome // factor)) == 3 and len(str(factor)) == 3:
			return True
	return False

largest_palindrome_product = 0
for num in range(10000, 1000000):
	if is_palindrome(num) and has_triple_digit_factors(num) and num > largest_palindrome_product:
		largest_palindrome_product = num
	
print(largest_palindrome_product)
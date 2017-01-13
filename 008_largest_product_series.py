large_num = open('./008_large_num.txt', 'r').read()
largest_product = 0

for start in range(len(large_num)):
	product = 1
	if start + 13 <= len(large_num) - 1:
		number_snippet = large_num[start:start+13]
	else: break
	
	for digit in number_snippet:
		product *= int(digit)
	if product > largest_product:
		largest_product = product
		
print(largest_product)
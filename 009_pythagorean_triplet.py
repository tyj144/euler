from math import sqrt
		
for a in range(1, 1000):
	for b in range(a + 1, 1000 - a):
		c = sqrt(a ** 2 + b ** 2)
		if c.is_integer() and a + b + c == 1000:
			print(int(a * b * c))
		
		
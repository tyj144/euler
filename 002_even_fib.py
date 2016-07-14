def fib_4mil(n=1, n_prev=1, sum=0):
	if n >= 4000000:
		return sum
	if n % 2 == 0:
		sum += n
	return fib_4mil(n + n_prev, n, sum)

print(fib_4mil())
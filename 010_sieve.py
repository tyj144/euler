# https://projecteuler.net/thread=10#1936
# by lassevk

marked = [0] * 2000000
value = 3
s = 2
while value < 2000000:
	# unmarked values are primes
    if marked[value] == 0:
        s += value
        i = value
        # mark off all multiples of primes
        while i < 2000000:
            marked[i] = 1
            i += value
    # skips even values
    value += 2
print(s)
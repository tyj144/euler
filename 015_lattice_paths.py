from math import factorial

# http://mathworld.wolfram.com/BinomialCoefficient.html
# The number of lattice paths from the origin to (a, b) is C(a + b, a)
def nCr(n, r):
	return factorial(n) / (factorial(r) * factorial(n - r))

def num_paths(grid_size):
	return int(nCr(2 * grid_size, grid_size))

print(num_paths(20))

# Recursive solution (exponential)
# p=0

# def traverse(i, j, n):
#     global p
#     if i >= n and j >= n:
#         p+=1
#         return 1
#     elif i == n:
#         traverse(i, j+1, n)
#     elif j < n:
#         traverse(i, j+1, n)
#         traverse(i+1, j, n)
#     else:
#         traverse(i+1, j, n)

# def num_paths(size):
#     traverse(0,0,size)
#     return p

# print(num_paths(3))
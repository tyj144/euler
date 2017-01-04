
collatz_len = 0

def len_collatz(n: int, collatz_len=0) -> int:
    n = int(n)
    collatz_len += 1
    if n == 1:
        return collatz_len
    elif n % 2 == 0:
        return len_collatz(n // 2, collatz_len)
    else:
        return len_collatz(3 * n + 1, collatz_len)


longest_chain = 0
num = 1
for i in range(1, 1000000):
    print(i // 100000, longest_chain)
    length = len_collatz(i)
    if length > longest_chain:
        longest_chain = length
        num = i

print(num)

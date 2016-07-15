collatz = []
def len_collatz(n: int) -> int:
    n = int(n)
    collatz.append(n)
    if n == 1:
        length = len(collatz)
        collatz.clear()
        return length
    elif n % 2 == 0:
        return len_collatz(n // 2)
    else:
        return len_collatz(3 * n + 1)


longest_chain = 0
num = 1
for i in range(1, 1000000):
    print(longest_chain)
    length = len_collatz(i)
    if length > longest_chain:
        longest_chain = length
        num = i

print(num)

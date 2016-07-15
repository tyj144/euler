nums = open('013_nums.txt', 'r').read().split('\n')
digits = ""

carry_over = 0
for index in range(len(nums[0]) - 1, -1, -1):
	s = sum(int(num[index]) for num in nums)
	s += carry_over
	if index <= 9:
		digits = str(s % 10) + digits
	carry_over = s // 10

digits = str(carry_over) + digits
digits = digits[:10]
print(digits)
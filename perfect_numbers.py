def find_perfects(num_h):
	li = []
	for num in range(1, num_h+1):
		num_s = 0
		for number in range(1, num//2):
			if num % number == 0:
				num_s += number
		if num_s == num:
			li.append(num_s)
	return li
		# else:
		# 	print(num, "is not a perfect number!")


print(find_perfects(10000))


# num = 9
# num_s = 0
# for number in range(1, num+1//2):
# 	if num % number == 0:
# 		num_s += number
# if num_s == num:
# 	print(num, "is a perfect number!")
# else:
# 	print(num, "is not a perfect number!")
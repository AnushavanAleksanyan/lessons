def sum_rec(lis):
	if len(lis)==1:
		return lis[0]
	else:
		return lis[0] + sum_rec(lis[1:])


ls = [1, 2, 3, 5, 7]

print(sum_rec(ls))
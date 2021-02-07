def mult(samp_list):
	total = 1
	for number in samp_list:
		total *= number
	return total



samp_l = [6, 2, -3, 1, 5]

print(mult(samp_l))
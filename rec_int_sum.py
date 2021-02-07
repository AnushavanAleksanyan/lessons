def sum_n(number):
	if number == 0:
		return 0
	else:
		return number%10 + sum_n(number//10)


number1 = 23
print(sum_n(number1))
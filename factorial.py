def fact(num):
	total = 1
	for number in range(1, num+1):
		total *= number
	return total


inp_num = int(input("input a number: "))

print(fact(inp_num))
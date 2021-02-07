def is_prime(number):
	if isinstance(number, int) and number > 0:
		for i in range(2, number):
			if number % i == 0:
				print ("False")
				break
			else:
				print ("True")
				break


inp_num = int(input("Input a number: "))
is_prime(inp_num)
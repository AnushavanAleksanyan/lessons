num = int(input("enter a nonnegative number: "))

num_str = str(num)
num_str = num_str[-2:]
num_str = int(num_str)
last_two_index = num_str//50*50
num_index = num//50*50
print(num_index+last_two_index)
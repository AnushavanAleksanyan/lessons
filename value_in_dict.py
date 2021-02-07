def find_value(value, dic):
	if value in list(dic.values()):
		return True
	else:
		return False

some_dic = {"one": "Monday", "two": "Tuesday", "three":"Wednesday", "four":"Thursday", "five":"Friday", "six": "Saturday", "seven": "Sunday"}
val = "Monday"


print(find_value(val, some_dic))
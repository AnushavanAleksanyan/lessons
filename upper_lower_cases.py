def up_low(sent):
	upper = 0
	lower = 0
	for letter in sent:
		if letter.isupper():
			upper += 1
		elif letter.islower():
			lower += 1
		else:
			pass
	print(f"Upper case characters: {upper}")
	print(f"Lower case characters: {lower}")


text = input("Type a sentense: ")

up_low(text)
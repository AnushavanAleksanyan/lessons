def find_substr(substr, text):  #finds and returns positions of first and last substring
	lst = []
	sub_length = len(substr)
	for index in range (len(text)):
		cut = slice(index, index+sub_length)
		if inp_text[cut] == substr:
			lst.append(index)
	return f"“{substr}” first position in “{text}” is {lst[0]}\n" \
	f"“{substr}” last position in “{text}” is {lst[-1]}"


inp_text = input("Type some text: ") # e.g. "it is fruit cocktail from italy"
sub_str = input("Enter a substring: ")  # e.g. "it"

print(find_substr(sub_str, inp_text))
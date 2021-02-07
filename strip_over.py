def strip_over(text, symb):  # removes the symbol from the beggining and the end
	for i in range(len(text)):  # cuts from the begining
		if text[i]  != symb:
			striped = text[i:]
			break
	for j in range(len(striped)):  # cuts from the end
		if striped[-j-1] != symb:
			striped = striped[:-j]
			return striped

txt = "aaaasdaafgaaaalkaaaa"
symbol = "a"

print(strip_over(txt, symbol))

# # extended

# def strip_over(text, s_str)->str:  # removes all symbols from the beggining and the end
# 	text = text.strip()
# 	for i in range(len(text)):  # cuts from the begining
# 		if text[i] not in s_str:
# 			striped = text[i:]
# 			break
# 	for j in range(len(striped)):
# 		if striped[-j-1] not in s_str:  # cuts from the end
# 			striped = striped[:-j]
# 			return striped


# txt = " abaaaskdaafkgaaaalkbaaaab"
# sub_str = "ab k"

# print(strip_over(txt, sub_str))
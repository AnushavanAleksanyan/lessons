def count_ints(li):
	count = 0
	for item in li:
		if isinstance(item, int):
			count += 1
		elif isinstance(item, (list, tuple)):
			for item1 in item:
				if isinstance(item1, int):
					count += 1
	return count



a = ["1", 1, "abc", 124.6, ["dfg", 2, 2.2], (3, 4, "zxc"), 12, "jkl", [5, "1"]]

print(count_ints(a))
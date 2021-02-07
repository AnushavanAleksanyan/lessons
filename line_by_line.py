def line_by_line(path):
	with open(path, "r") as f:
		li = [line for line in f]
		return li

print(line_by_line("4copies.py"))
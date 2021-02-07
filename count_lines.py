def count_lines(path):
	with open(path, "r") as f:
		print(len(f.readlines()))

count_lines("factorial.py")
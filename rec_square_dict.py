def square_dict(n: int)->dict:
	if n == 0:
		return 1
	else:
		square_dict(n-1)
		dct.update({n: n*n})
	return dct

dct={}

print(square_dict(8))
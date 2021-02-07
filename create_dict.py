def merge_dict(dict_n, *dicts):
	for elem in range(len(dicts)):
		dict_n.update(dicts[elem])
	return dict_n


dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic_n = dict()

print(merge_dict(dic_n, dic1, dic2, dic3))
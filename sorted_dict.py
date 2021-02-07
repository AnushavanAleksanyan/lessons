def sort_by_value(a_dict):
	sorted_dict={key: value for key, value in sorted(a_dict.items(), key = lambda key: key[1])}
	return sorted_dict

this_dict = {"name3": "Mike", "name2": "Joe", "name9" : "Alex", "name1" : "Jeck", "name7" : "Denny",  "name8" : "Albert"}

print(sort_by_value(this_dict))

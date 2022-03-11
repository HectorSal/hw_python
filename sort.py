def sort_list(list):
	n = len(list)
	if n = 0:
		return list
	object_type = type(list[0])
	for i in range(n):
		if object_type != type(list[i]):
			print("list contains different data types and cannot be sorted")
			return
	i = 0
	while i < n:
		j = 0
		while j < n - i - 1:
			if list[j] > list[j + 1]:
				temp = list[j]
				list[j] = list[j+1]
				list[j+1] = temp
			j = j + 1
		i = i + 1
	return list

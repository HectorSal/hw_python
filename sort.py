def sort_list(list):
	n = len(list)
	for i in range(n):
		try:
			list[i] = int(list[i])
		except:
			print("list contains input is not of int type")
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

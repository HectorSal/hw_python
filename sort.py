def sort_list():
	list_input = input()
	list = list_input.split(", ")
	n = len(list)
	for i in range(n):
		list[i] = int(list[i])
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

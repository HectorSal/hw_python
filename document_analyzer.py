document = open('document.txt', 'r')
test = document.read()
list = test.split(" ")
list = sorted(list) # sorted the words
n = len(list)
word_count = {}
for i in range(n):
	word_count[list[i]] = list.count(list[i])
# I have created a dictionary with each word mapped to the number of occurences
word_count_values = word_count.values()
word_count_values = sorted(word_count_values, reverse = True) # sorted values

word_count_values_no_duplicates = list(dict.fromkeys(word_count_values))

word_count_sorted = {}
#go through each value starting from the largest value and add the word that maps to that value to a new dictionary
for i in range(n):
	for key in word_count:
		if word_count.get(key) == word_count_values_no_duplicates[i]:
			word_count_sorted[key] = word_count_values_no_duplicates[i]
print('\r')
i = 0
for key in word_count_sorted:
	if i < 5:
		print(f"{key}: {word_count_sorted.get(key)}")
	else:
		break
	i = i + 1

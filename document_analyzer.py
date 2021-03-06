document = open('document.txt', 'r')
document_text = document.read()
list = document_text.split(" ")
list = sorted(list) # sorted the words
n = len(list)
word_count = {}
for i in range(n):
	word_count[list[i]] = list.count(list[i])
# I have created a dictionary with each word mapped to the number of occurences
word_count_values = word_count.values()
word_count_values = sorted(word_count_values, reverse = True) # sorted values

n = len(word_count_values)
# use a for loop to add the values to a dictionary. The dictionary will have no duplicates, so its keys can be put in a list.
no_duplicate_values = {}
for i in range(n):
	no_duplicate_values[word_count_values[i]] = i
word_count_values_no_duplicates = []
word_count_values_no_duplicates.extend(no_duplicate_values.keys())
n = len(word_count_values_no_duplicates)

word_count_sorted = {}
#go through each value starting from the largest value and add every word that maps to that value to a new dictionary
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

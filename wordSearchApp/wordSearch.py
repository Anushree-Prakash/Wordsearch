import operator

word_count = {}
words = []
with open('word_search.tsv') as datafile:  
	for row in datafile:
		word, frequency = row.split('\t')  
		word_count[word] = int(frequency.strip())
		words.append(word)  

def search(word_letter):
	results = []
	for word in words:
		if word_letter in word:
			results.append(word)
	return results

def sorting(results, incomplete_word):
	result_distances = [(result, result.find(incomplete_word),
	                     word_count[result], len(result)) for result in results]
	result_distances.sort(key=operator.itemgetter(1))
	result_distances.sort(key=operator.itemgetter(3))
	searchResults = [result_distance[0]
                  for result_distance in result_distances][:25]
	return searchResults
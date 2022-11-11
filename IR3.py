# Stop word removal
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = """This is a sample sentence,
				which filters out stop words"""

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

filtered_sentence = []

for w in word_tokens:
	if w not in stop_words:
		filtered_sentence.append(w)

# Combine all the words again
final_sentence = ' '.join(filtered_sentence)

print(word_tokens)
print(filtered_sentence)
print(final_sentence)
# Program to compare similarity of 2 documents
import math
import string
from collections import defaultdict

# Function to read the documents
def read_file(filename):
	with open(filename, 'r') as f:
		data = f.read()
	return data

# Using default functions to remove punctuations and convert into lowercase letters
conversion = str.maketrans(string.punctuation," "*len(string.punctuation))
conversion = str.maketrans(string.ascii_uppercase,string.ascii_lowercase)

# Convert the text from documents to a list of words
def get_words_from_line_list(text):
	text = text.translate(conversion)
	word_list = text.split()
	
	return word_list

# Function to count frequency of words in document
def count_frequency(word_list):
	D = defaultdict(int)
	for new_word in word_list:
		if new_word in D:
			D[new_word] = D[new_word] + 1
		else:
			D[new_word] = 1
			
	return D

# Create a word to word to frequency mapping
def findFrequency(filename):
	line_list = read_file(filename)
	word_list = get_words_from_line_list(line_list)
	freq_mapping = count_frequency(word_list)

	return freq_mapping

# Function to find the dot product of 2 vectors
def dotProduct(D1, D2):
	Sum = 0.0
	for key in D1:		
		if key in D2:
			Sum += (D1[key] * D2[key])
	
	return Sum

# Function to find angle between vectors
def vector_angle(D1, D2):
	numerator = dotProduct(D1, D2)
	denominator = math.sqrt(dotProduct(D1, D1)*dotProduct(D2, D2))
	# Use formula:
	# cos(x) = D1.D2 / |D1|.|D2|
	return (math.acos(numerator / denominator)*180/(math.pi))


def findSimilarity(filename_1, filename_2):
	wordList1 = findFrequency(filename_1)
	wordList2 = findFrequency(filename_2)
	Angle = vector_angle(wordList1, wordList2)
	
	print("The Angle between the documents is: % 0.2f (degrees)"% Angle)
	
# Call the main function
findSimilarity('file1.txt', 'file2.txt')

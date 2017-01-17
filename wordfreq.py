#program for frequency distribution of words from text file. 
file = open('nlptext.txt','r')
test_str = file.read()

word_freq = {}

for tok in test_str.split():
	if tok in word_freq:
		word_freq[tok] += 1
	else:
		word_freq[tok] = 1

print word_freq

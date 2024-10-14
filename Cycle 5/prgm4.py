from nltk import ngrams
sentence = 'I reside in India'
n = 2
trigrams = ngrams(sentence.split(),n)
for grams in trigrams:
    print(grams)
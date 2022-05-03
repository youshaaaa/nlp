# Implement Filtration, Script Validation, Stop Word Removal in Python

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

f = open("text.txt","r")

#wordtokenizer
for line in f:
 print("Tokenization without NLTK \n")
 print(line.split())
 print("Length of Tokenization without NLTK:")
 print(len(line.split()))
 print("Tokenization with NLTK \n")
 print(word_tokenize(line))
 print("Length of Tokenization with NLTK:")
 print(len(word_tokenize(line)))

#filteration
 print("Filteration \n")
 bad_chars = [';',',','!',':','*','#','<','>','?','@','.']
 words = word_tokenize(line)

 print(list(filter(lambda i: i not in bad_chars,words))) ## remember the syntax of lambda fn
 print("Length of Filteration:")
 print(len(list(filter(lambda i: i not in bad_chars,words))))

#stop word removal
 print("Stop word removal \n")
 stop_words = set(stopwords.words("English"))
 without_stop_words = [word for word in words if not word in stop_words]
 with_stopwords = list(filter(lambda i: i not in bad_chars, without_stop_words)) #??
 print(with_stopwords)
 print("Length of Stopword Removal:")
 print(len(with_stopwords))

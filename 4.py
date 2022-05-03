#stemming and lemmatization
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
f = open("text1.txt","r")

#wordtokenizer
for line in f:
 print("Tokenization without NLTK \n")
 print(line.split())
 print("\n")
 print("Length of Tokenization without NLTK:")
 print(len(line.split()))
 print("\n")
 print("Tokenization with NLTK \n")
 print(word_tokenize(line))
 print("\n")
 print("Length of Tokenization with NLTK:")
 print(len(word_tokenize(line)))
 print("\n")

#filteration
 print("Filteration \n")
 bad_chars = [';',',','!',':','*','#','<','>','?','@','.']
 words = word_tokenize(line)
 print(list(filter(lambda i: i not in bad_chars,words)))
 print("\n")
 print("Length of Filteration:")
 print(len(list(filter(lambda i: i not in bad_chars,words))))
 print("\n")

#stop word removal
 print("Stop word removal \n")
 stop_words = set(stopwords.words("English"))
 without_stop_words = [word for word in words if not word in stop_words]
 with_stopwords = list(filter(lambda i: i not in bad_chars, without_stop_words))
 print(with_stopwords)
 print("\n")
 print("Length of Stopword Removal:")
 print(len(with_stopwords))
 print("\n")

#Stemming and Lemmatization
 ps = PorterStemmer()
 l = WordNetLemmatizer()

#Tablular form to compare
 print("Word \t \tStemming \tLemmatization")
 for w in with_stopwords:
    print ("{:<15} {:<15} {:<15}".format( w, ps.stem(w), l.lemmatize(w)))
 print("\n")
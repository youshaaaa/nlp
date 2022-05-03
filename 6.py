# N-gram model in python to predict sentence probability.

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from collections import Counter

f = open("text2.txt","r")
for line in f:
 l1=[] #Count of bigrams
 l2=[] #First word of bigram
 l3=[] #Probability of bigram
 l4=[] #tuples of bigrams 
 prod = 1

#wordtokenizer
 print("Tokenization with NLTK \n")
 print(word_tokenize(line))
 print("\n")

#Filteration
 print("Filteration \n")
 bad_chars = [';',',','!',':','*','#','<','>','?','@','.']
 words = word_tokenize(line)
 swords = []
 swords = list(filter(lambda i: i not in bad_chars,words))
 print(swords)
 print("\n")
 pair_words = []

#Bigram generation 
 for i in range(len(swords)-1):
    pair_words.append((swords[i],swords[i+1]))
 print("The bi-grams are:")
 print(pair_words)
 print("\n")

 cnt = dict(Counter(pair_words))
 print("Count of occurances of bigrams")
 for pair, number in cnt.items():
    l1.append(number)
    l2.append(pair[0])
    l4.append(pair)
    print(pair, ":", number)
 print("\n")

 print("Probability of the bigrams")
 for x in range(len(l2)):
    p = swords.count(l2[x])
    l3.append(round(l1[x]/p,3))
    prod = l3[x]*prod
    print(l4[x], ":", l3[x])
 print("\n")

 print("Probability of the sentence.")
 print(prod) 

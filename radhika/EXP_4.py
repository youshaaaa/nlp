import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk import word_tokenize
from nltk.stem.porter import *
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag

sentence1 = input("Enter your sentence: ")
ps=PorterStemmer()
print("Stemming in process\n")
tokens=word_tokenize(sentence1)
for word in tokens:
    print(word+":"+ ps.stem(word))

sentence2 = input("Enter your sentence: ")
lemmatizer = WordNetLemmatizer()
print("Lemmatization in process\n")
tokens=word_tokenize(sentence2)
tags=['n','v','a']
for word in tokens:
    lemma=[]
    for tag in tags:
        lemma.append(lemmatizer.lemmatize(word, tag))
    print(word,'--->',lemma)

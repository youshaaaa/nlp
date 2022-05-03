# Implement Morphological Analysis

import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob

# nltk.download('omw-1.4') #error in my system solved by adding this line

#Morphological Analysis
def get_wordnet_pos(word):
 tag = nltk.pos_tag([word])[0][1][0].upper()
 tag_dict = {"J":wordnet.ADJ,
 "N":wordnet.NOUN,
 "V":wordnet.VERB,
 "R":wordnet.ADV}
 return tag_dict.get(tag,wordnet.NOUN)
f=open("text1.txt")
stop_words = set(stopwords.words("English"))
bad_chars = (';',':','!', "*",'<','>','#','?','@','p',',','.','(',')','eos')
for line in f:
 words = word_tokenize(line)
 print("Word Tokenization\n")
 print(words)
 print("\n")
 #stop word and filterization
 without_stop_words = [word for word in words if not word in stop_words]
 ws = list(filter(lambda i: i not in bad_chars,without_stop_words))
 print("Filtered Words \n")
 print(ws)
 print("\n")
 ws_tag = nltk.pos_tag(ws)
wordtaglength = len(ws_tag)
#Lemmatizer 
l = WordNetLemmatizer()
print("WORD","\t\t\t","ROOT WORD(MORPHENE)","\t\t","TAG")
for i in range(wordtaglength): 
 print(ws[i].ljust(9),"\t\t",l.lemmatize(ws[i],get_wordnet_pos(ws[i])).ljust(9),"\t\t",ws_tag[i])

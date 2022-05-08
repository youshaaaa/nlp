from itertools import count
import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
file=input("ENTER:")
words=(word_tokenize(file))
bad_chars=[';',':','!','*','.','#','&','@','<','>','^']
for w in words:
    if w in bad_chars:
        words.remove(w)
    print(words)
stops = set(stopwords.words("english"))
final = []
for w in words:
    if w not in stops:
        final.append(w)
    print(final)
print("words with stop words=",len(words))
print("words without stop words=",len(final))

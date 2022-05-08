import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
#Filter Words
sent = '''The cat caught by the spider that caught the fly the old lady swallowed.
The fly swallowed by the old lady was caught by the spider caught by the cat.
The fly the spider the cat caught was swallowed by the old lady'''
stop_words = set(stopwords.words('english'))
words = word_tokenize(sent)
filtered_words = [w.lower() for w in words if not w.lower() in stop_words]
print (filtered_words)
#POS Tagging
tagged = pos_tag(filtered_words)
#Chunking
grammar = ("NP: {<VB|VBD|VBP>?<JJ>*<NN>} # NP")
chunkParser = nltk.RegexpParser(grammar)
tree = chunkParser.parse(tagged)
print(tree)

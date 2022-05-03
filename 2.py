import re # regex library
from nltk.tokenize import word_tokenize,sent_tokenize
from pathlib import Path

text = Path('text.txt').read_text()
tokens = re.findall("[\w']+", text)
print("Word Tokenization without NLTK:\n")
print(tokens)
print("\nWord TOkenization with NLTK:\n")
print(word_tokenize(text))
print("\nSentence Tokenization without NLTK\n")
sentences = text.split('. ')
print(sentences)
print("\nSentence Tokenization with NLTK\n")
print(sent_tokenize(text))

#  implement Sentence and Word Tokenization in python.
# /w is a word character i.e. [a-zA-Z0-9_]
# /W is a non word character i.e. [^a-zA-Z0-9_]

"""
this is a comment
over mutiple
lines
"""

# """ are for spanning multiple lines of text.
# tabs, \n etc can be used inside """


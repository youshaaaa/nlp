import nltk
nltk.download('punkt')
from collections import Counter
from collections import defaultdict
from nltk.corpus import brown
from nltk.util import ngrams
from nltk.lm.preprocessing import pad_both_ends
import string


text = '''He said how are you. I said I am fine. I asked how he was. He said 
he was feeling terrible.'''
bigrams = []
words = []

sent_token= nltk.sent_tokenize(text)
for sent in sent_token:
    word_token= nltk.word_tokenize(sent)
    token_word=list(filter(lambda x: x not in string.punctuation, word_token))
    token_word=list(u.lower() for u in token_word)
    words.extend(['<s>','</s>'])
    words.extend(token_word)
    bigrams.extend(list(ngrams(pad_both_ends(token_word,n=2),n=2)))
print(bigrams)

bigrams_freq = Counter(bigrams)
words_freq = Counter(words)
print(f'{" "*6}|', end='')
print("|".join([f"{word:^6}" for word in words_freq.keys()]))
print(f'{"-"*6}|' * (1+len(words_freq.keys())), end="")

for word_row in words_freq:
    print(f"\n{word_row:^6}|", end='')
    for word_column in words_freq:
        print(f'{bigrams_freq[(word_row,word_column)]:^6}',end='|')
print('')
print('')
print(f'{" "*6}|', end='')
print('|'.join([f'{word:^6}' for word in words_freq.keys()]))
print(f'{"-"*6}|'*(1+len(words_freq.keys())), end='')
bigrams_prob = defaultdict(int)

for gram in bigrams_freq.keys():
    bigrams_prob[gram]=bigrams_freq[gram]/words_freq[gram[0]]

for word_row in words_freq:
    print(f'\n{word_row:^6}|', end='')
    for word_column in words_freq:
        print(f'{bigrams_prob[(word_row,word_column)]:6}',end='|')
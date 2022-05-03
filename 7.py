#  Implement POS Tagging using Hidden Markov Model

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.util import ngrams
from nltk.lm.preprocessing import pad_both_ends
from collections import Counter
import numpy as np
import pandas as pd
import string

text = '''Marry Jane can see Will.
Spot will see Mary.
Will Jane spot Mary?
Mary will pat Spot.'''
sent_text = nltk.sent_tokenize(text)
tagged_sents = []
tags_transitions = []
uni_tags = []
for sent in sent_text:
    tokenized_words = word_tokenize(sent)
    tokens = list(filter(lambda token: token not in string.punctuation, tokenized_words))
    tokens = list(x.lower() for x in tokens)
    tagger = nltk.pos_tag(tokens)
    tagged_sents.extend(tagger)
    tags_transition = [tup[1] for tup in tagger]
    uni_tags.extend(tags_transition + ['<s>', '</s>'])
    tags_transitions.extend(list(ngrams(pad_both_ends(tags_transition, n=2), n=2)))
print("Tagged Sentences :\n",tagged_sents)

tagged_words = [ tup for tup in tagged_sents ]
count_tagged_words = Counter(tagged_words)
tags = list({tag for word, tag in tagged_words})
vocabs = {word for word, tag in tagged_words}
print("\nTags: ",tags)
print("\nVocabs: ",vocabs)
em = pd.DataFrame({tag: [] for tag in ["Words"]+tags})

print("\nEMISSION")
for vocab in vocabs:
    em.loc[vocab] = [vocab] + [count_tagged_words[vocab, tag] for tag in tags]
em.set_index('Words')
print("\nFrequency :\n",em)
tag_freq_em = Counter(elem[1] for elem in tagged_sents)
for vocab in vocabs:
    for tag in tags:
        em.at[vocab, tag] /= tag_freq_em[tag]
print("\nProbability :\n",em)
print("\nTRANSITION")
tags_trans_freq = Counter(tags_transitions)
tr = pd.DataFrame({tag: [] for tag in ["Tags"]+tags+["</s>"]})
for tag_row in ["<s>"]+tags:
    tr.loc[tag_row] = [tag_row] + [tags_trans_freq[tag_row, tag_col] for tag_col in tags+["</s>"]]
tr.set_index('Tags')
print("\nFrequency :\n",em)
tag_freq_tr = Counter(uni_tags)
for tag_row in ["<s>"]+tags:
    for tag_col in tags+["</s>"]:
        tr.at[tag_row, tag_col] /= max(1,tag_freq_tr[tag_row])
tr.set_index('Tags')
print("\nProbability :\n",em)

wrong_tag = [('will', 'MD'),
('can', 'VB'),
('spot', 'NN'),
('mary', 'NN')]
wrong_tags = [tup[1] for tup in wrong_tag]
wrong_tags_pairs = list(ngrams(pad_both_ends(wrong_tags, n=2), n=2))
print("\nWrong Tags Pairs : ", wrong_tags_pairs)

prob = 1
for pair in wrong_tags_pairs:
    prob *= tr.at[pair[0], pair[1]]
print("\nProbability of Correct Sentence:",prob)

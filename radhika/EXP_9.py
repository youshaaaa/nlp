import nltk
sentence = """India, officially the Republic of India (Hindi: Bhārat Gaṇarājya), 
is a country in South Asia. It is the seventh-largest country by area, 
the second-most populous country, and the most populous democracy in the world. 
Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, 
and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;
[f] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. 
In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; 
its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar and 
Indonesia.""" 
for sent in nltk.sent_tokenize(sentence):
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
        if hasattr(chunk, 'label'):
            print(chunk.label(), ' '.join(c[0] for c in chunk))

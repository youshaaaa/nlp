import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

#Morphological Analysis

#Filtration
sent = "The Avengers. It is what we call ourselves. Sorta liking a team. Mightiest Heroes of the Earth type thing."
stop_words = set(stopwords.words('english'))
words = word_tokenize(sent)
filtered_words = [w.lower() for w in words if not w.lower() in stop_words]
print (filtered_words)

#Lemmatization
lemmatizer = WordNetLemmatizer()
print(f'{"Word":^8} --> {"Lemma":^8}')
print(f'{"-"*8}-----{"-"*8}')
for word in filtered_words:
    print(f'{word:^8} --> {lemmatizer.lemmatize(word):^8}')
#POS Tagging
tagged = pos_tag(filtered_words)
print (tagged)

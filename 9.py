# implement Named Entity Recognition for given corpus in python

import spacy
from spacy import displacy
from collections import Counter\

nlp = spacy.load('en_core_web_sm')
doc = nlp('''Manchester United Football Club is a professional football club based in Old Trafford, Greater Manchester, England, that competes in the Premier League, the top flight of English football. Nicknamed the Red Devils, the club was founded as Newton Heath LYR Football Club in 1878, but changed its name to Manchester United in 1902. The club moved from Newton Heath to its current stadium, Old Trafford, in 1910. Manchester United have won the joint-record number of trophies in English club football, including a record 20 League titles, 12 FA Cups, five League Cups and a record 21 FA Community Shields.''')
l1 = list([(X.text, X.label_) for X in doc.ents])
print(*l1, sep = "\n")

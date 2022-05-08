import nltk
from nltk.corpus import brown
# nltk.download('brown')
brown_word_tags = []
# Manually add start and end tags for each sequence
for brown_sent in brown.tagged_sents():
    brown_word_tags.append(('START', 'START'))
    for words, tag in brown_sent:
        brown_word_tags.extend([(tag[:2], words)])
    brown_word_tags.append(('END', 'END'))
# get conditional freq distribution for brown word tags
cfd_tag_words = nltk.ConditionalFreqDist(brown_word_tags)

#get conditional probalilty distribution for the tag words obtained
cpd_tag_words = nltk.ConditionalProbDist(cfd_tag_words, nltk.MLEProbDist)
print("Emission Probabilities:")
print("The probability of an adj(JJ) being 'smart' is ", cpd_tag_words["JJ"].prob("smart"))
print("The probability of an verb(VB) being 'try' is ", cpd_tag_words["VB"].prob("try"))
print("The probability of an possesive pronoun(PP) being 'I' is ", cpd_tag_words["PP"].prob("I"))
# Estimating P(ti | t(i-1)) from corpus data using maximum likelyhood estimation(MLE)
# P(ti | t(i-1)) = count(t(i-1), ti) / count(t(i-1))
brown_tags = []
for tag, words in brown_word_tags:
    brown_tags.append(tag)
# make conditional freq distri
# count(t(i-1), ti)
cdf_tags = nltk.ConditionalFreqDist(nltk.bigrams(brown_tags))
# make conditional prob distri using MLE
# P(ti | t(i-1))
cpd_tags = nltk.ConditionalProbDist(cdf_tags, nltk.MLEProbDist)
print("Tag Transition Probabilities:")
print("The probability of DT occuring after NN is : ", cpd_tags['NN'].prob('DT'))
print("The probability of VB occuring after NN is : ", cpd_tags['NN'].prob('VB'))
prob_tagsequence = cpd_tags["START"].prob("PP") * cpd_tag_words["PP"].prob("I") * cpd_tags["PP"].prob("VB") * cpd_tag_words["VB"].prob("love") * cpd_tags["VB"].prob("NN") * cpd_tag_words["NN"].prob("food") * cpd_tags["NN"].prob("END")
print("The probability of the sentence 'I love food' having the tag sequence 'START PP VB NN END' is : ", prob_tagsequence)
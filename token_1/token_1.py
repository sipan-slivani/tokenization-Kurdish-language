
import nltk
import arabic_reshaper
from nltk import sent_tokenize
from nltk import word_tokenize
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from bidi.algorithm import get_display


text_file = open(u"ttt.txt")
text = text_file.read()
#text = arabic_reshaper.reshape(text)
#text = get_display(text)
sentence = sent_tokenize(text)
#print(len(sentence))
#print(sentence)
sentence
#krd = u"ناڤی من سیپانە"
#krd = get_display(krd)
#print(krd)

#text = text_file.read()
words = word_tokenize(text)
#print(len(words))
#print(words)


#words
word_nop = []

for w in words:
    if w.isalpha():
        word_nop.append(w.lower())

#print(word_nop)
#print(len(word_nop))
#word_nop = arabic_reshaper.reshape(word_nop)
#word_nop = get_display(word_nop)  

fdist = FreqDist(word_nop)
#fdist.
fw = fdist.most_common(15)
print(fw)
fdist.plot(15)

text_file.close()
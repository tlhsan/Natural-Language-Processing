import nltk
from nltk.tokenize import word_tokenize

example = " Google "
words = word_tokenize(example)

for w in words:
    words_tokens = nltk.word_tokenize(w)
    tagged = nltk.pos_tag(words_tokens)
    #print(tagged)
    namedEnt = nltk.ne_chunk(tagged)
    namedEnt.draw()
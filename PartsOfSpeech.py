import nltk
from nltk.tokenize import word_tokenize

example = "My name is Taruha Sama. I work at Inttelisearch. My hobby is to play foorball. I love my family. I study in Brac university. I want to live in Japan."
words = word_tokenize(example)

for w in words:
    words_tokens = nltk.word_tokenize(w)
    tagged = nltk.pos_tag(words_tokens)
    print(tagged)
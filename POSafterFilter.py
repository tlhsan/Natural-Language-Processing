import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

ps = PorterStemmer()
example = "My name is Taruha Sama. I work at Inttelisearch. My hobby is to play foorball. I love my family."
words = word_tokenize(example)
stop_words = set(stopwords.words('english'))
without_stopwords = []
final_words = []
for w in words:
    if w not in stop_words:
        without_stopwords.append(w)

for w in without_stopwords:
    final_words.append(ps.stem(w))

for w in final_words:
    tokens = nltk.word_tokenize(w)
    tagged = nltk.pos_tag(tokens)
    print(tagged)


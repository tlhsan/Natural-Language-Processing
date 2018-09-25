from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example = "my name is Talha. I live in Japane, i mean very soon going to live there. bye!"
stop_words = set(stopwords.words("english"))
words = word_tokenize(example)
filtered_words = []
for w in words:
    if w not in stop_words:
        filtered_words.append(w)

print(filtered_words)


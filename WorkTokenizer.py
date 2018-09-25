from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps = PorterStemmer()
#example = "my name is Talha. I live in Japan, i mean very soon going to live there. bye!"
stop_words = set(stopwords.words("english"))
example = input("Enter the text to be classified")
result = word_tokenize(example)
filtered_words = []
final_words =[]
for w in result:
    if w not in stop_words:
        filtered_words.append(w)

for w in filtered_words:
    final_words.append(ps.stem(w))


print(final_words)
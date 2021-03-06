import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()
stop_words = set(stopwords.words("english"))
text = input("please enter thr text \n")
words = word_tokenize(text)
filtered_words=[]
final_words=[]

for w in words:
    if w not in stop_words:
        filtered_words.append(w)

for w in filtered_words:
    final_words.append(lemmatizer.lemmatize(w))

# now tag the POS for the final words

for w in final_words:
    word_tokens = nltk.word_tokenize(w)
    tagged = nltk.pos_tag(word_tokens)
    entity_extraction = nltk.ne_chunk(tagged)
    print(entity_extraction)


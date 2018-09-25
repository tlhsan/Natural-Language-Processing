from nltk.stem import PorterStemmer
 #from nltk.tokenize import word_tokenize

ps= PorterStemmer()
words = ["play", "Playing", "Playful", "playly"]
for w in words:
    print(ps.stem(w))
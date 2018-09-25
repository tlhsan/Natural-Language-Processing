from nltk.corpus import wordnet
syns = wordnet.synsets("good")
print(syns[0].definition())
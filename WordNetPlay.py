import nltk
from nltk.corpus import wordnet



#for w in syn:
 #   for l in w.lemmas():
#        synonyms.append
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")

print(w1.wup_similarity(w2))
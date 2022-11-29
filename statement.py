import os
import re

class statement_tokenizer:
    
    def __init__(self):
        self._pattern='r"[A-Z]+[a-z]*\s\."'
        self._regex = re.compile(self._pattern)
        self._tokens=[]
        
    def get_tokens(self, text) -> list:
        self._tokens= self._regex.split(text)
        return self._tokens
    
    def __str__(self) -> str:
        for s in self._tokens:
          print(f"statement -> {s}")
        
        import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))


# txt = "Knowing Abdoul Azis is a curse"

with open('sales.txt') as f:
    contents = f.read()

# sent_tokenize is one of instances of
# PunktSentenceTokenizer from the nltk.tokenize.punkt module

tokenized = sent_tokenize(contents)

tagged =[]
for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(wordsList)
parts = []
for pair in tagged:
        if pair[1] == "NNP" or pair[1] == "NNS" or pair[1] == "NNPS" or pair[1] == "NN":
            parts.append("noun")
        elif pair[1] == "VB" or pair[1] == "VBD" or pair[1] == "VBG" or pair[1] == "VBN" or pair[1] == "VBP" or pair[1] == "VBZ":
            parts.append("verb")
        elif pair[1] == "JJ" or pair[1] == "JJR" or pair[1] == "JJS":
            parts.append("adjective")
        elif pair[1] == "DT":
                parts.append("Determinant")
        else:
            parts.append(pair[1])
            
print(parts)

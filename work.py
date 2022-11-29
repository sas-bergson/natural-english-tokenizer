import nltk

filename = "./ggg.txt"
file = open(filename, "r")
text = file.read()


tokenized = nltk.sent_tokenize(text)
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
        else:
            parts.append(pair[1])
print(parts)
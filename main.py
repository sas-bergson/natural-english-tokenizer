
import nltk
from nltk.tokenize import word_tokenize

text1 = "This is a test desighned to verify the behavior\of the tokenizer.if it succeeds we will move to the design of the file scanner"
result = word_tokenize(text1)
print(result)
""""returns tokens from text"""
final = nltk.pos_tag(result)
print(final)
"""function  interpret the acronyms from the result"""
nltk.help.upenn_tagset("NN")
for i in range(0,len(final)):
    if (final[i][1] == "NN"):
        print(final[i][0])
""""returns loop of all words that are nouns"""
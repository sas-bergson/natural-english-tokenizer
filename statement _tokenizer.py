import os
import re
import json

data = json.load(open('letter_q_dictionary.json'))

class statement_tokenizer:

    statement = input("Enter your text: ")
    tokens = re.split("[\.!?]", statement)
    noc = len(statement)
    print("Total Number of Tokens: ", noc)


    def __init__(self, statement, tokens):
     self.statement = statement
     self.tokens =tokens


    for s in tokens:

        m = re.findall(r'\bq\w+', s)

        print("statement-- ", s, m)





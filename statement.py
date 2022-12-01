import os
import re

class statement_tokenizer:

    def __init__(self):
        """
        Here the it's a function with regex that is to is able to bring out the seperate statements that exist in a text
        """
        self._pattern='r"[A-Z]+[a-z]*\s\."'
        self._regex = re.compile(self._pattern)
        self._tokens=[]
        
    def get_tokens(self, text) -> list:
        """Here the split function now splits these statements into  seperate words """
        self._tokens= self._regex.split(text)
        return self._tokens
    
    def __str__(self) -> str:
        """It is overiding default string for python platform to understand"""
        for s in self._tokens:
          print(f"statement -> {s}")

text = "Man na strong man"
obj=statement_tokenizer()
print(obj.get_tokens(text))

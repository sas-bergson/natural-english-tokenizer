import os
import re

class statement_tokenizer:
    
    def __init__(self):
        #self._pattern='r"[A-Z]+[a-z]*\s\."'
        self._pattern='r"[A-Z]+[a-z]*\s\."'
        self._regex = re.compile(self._pattern)
        self._tokens=[]
        
    def get_tokens(self, text) -> list:
        #self._tokens= self._regex.split(text)
        self._tokens = text.split()
        return self._tokens
    
    def __str__(self) -> str:
        for s in self._tokens:
          print(f"statement -> {s}")
    
    
          
test = statement_tokenizer()
        
def pro():
    test.get_tokens("Hi my name is Yan")
    test.__str__()
    #print(test._tokens)

pro()
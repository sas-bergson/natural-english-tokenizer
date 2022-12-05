import os
import re

class statement_tokenizer:
    
    def __init__(self):
        self._pattern='r"[A-Z]+[a-z]*\s\."'
        self._regex = re.compile(self._pattern)
        self._tokens=[]
        
   
    
      
    

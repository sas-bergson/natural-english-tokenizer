import os
import re

class Tokenizer:
    
    def __init__(self):
        self._stmt_pattern='[\w*\s]*[\.|\?|,|;]? ?'
        self._token_pattern='\w*|\s*|[\.|\?|,|;]'
        self._statements=[]
        self._tokens=[]
    
    def get_statements(self, text) -> list:
        regex = re.compile(self._stmt_pattern)
        self._statements = regex.findall(text)
        for s in self._statements:
            if (len(s)==0): self._statements.remove(s) 
        return self._statements
        
    def get_tokens(self, text) -> list:
        regex = re.compile(self._token_pattern)
        self._tokens= regex.findall(text)
        for t in self._tokens:
            if (len(t)==0): self._tokens.remove(t) 
        return self._tokens
    
    def __str__(self) -> str:
        ret=''
        for s in self._statements:
            ret += f"statement -> {s} length = len(s)\n"
        for t in self._tokens:
                ret += f"token -> {t} (length = {len(t)})\n"
        return ret
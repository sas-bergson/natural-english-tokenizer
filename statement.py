import os
import re

class statement_tokenizer:
    
    def __init__(self):
        """This method is the constructor. where all the regex are defined and the word that the user or the calling file will use to call the method."""
        #self._pattern='r"[A-Z]+[a-z]*\s\."'
        self._pattern='r"[A-Z]+[a-z]*\s\."'
        self._regex = re.compile(self._pattern)
        self._noun_regex = re.compile(r"[a-zA-Z][0-9]*")
        self._sentences = []
        self._tokens=[]
        
    def get_tokens(self) -> list:
        """This method is responsible for the splitting of the individual strings into the required tokens which takes text the text that is to be split into tokens. and returns a list of tokens."""
        #self._tokens= self._regex.split(text)
        for s in self._sentences:
            print(s)
            self._tokens = s.split()
        return self._tokens
    
    def list_sentences(self):
        """"This method is responsible for printing the different sentences present in the text"""
        for s in self._sentences:
            print(f"sentence -> {s}")
    
    def get_sentence(self, text):
        """"This method is responsible for splitting a text block in the the different sentennces composing it"""
        self._sentences = text.split(". ")
        return self._sentences
    
    def __str__(self) -> str:
        """This method is responsible for the printing of the tokens that are returned by the get_tokens method.it takes no arguments and returns a string of the tokens."""
        for s in self._tokens:
          print(f"statement -> {s}")
          
    def tokenize_tokens(self):
        for s in self._tokens:
            if re.match(self._noun_regex, s):
                print(s, "Matched the regex")
            else:
                print(s, "Did Not Match the regex")
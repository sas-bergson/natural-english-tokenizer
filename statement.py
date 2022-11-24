
import os
import re

"""! @brief Example Python program with Doxygen style comments."""


class statement_tokenizer:
    def __init__(self):
        """
        This method is the constructor. where all the regex are defined and the word that the user or the calling file will use to call the method."""
        self._pattern = 'r"[A-Z]+[a-z]*\s\."'
        self._sentence_pattern = r'([A-Z][^\.!?]*[\.!?])'
        self._regex = re.compile(self._pattern)
        self._tokens = []

    def get_tokens(self, text) -> list:
        """
        This method is responsible for the splitting of the individual strings into the required tokens which
        takes  text (string) the text that is to be split into tokens. and returns a list of tokens."""
        self._tokens = self._regex.split(text)
        return self._tokens

    def __str__(self) -> str:
        """
        This method is responsible for the printing of the tokens that are returned by the get_tokens method.
        it takes no arguments and returns a string of the tokens. it basically overites the default __str__ method."""
        for s in self._tokens:
            print(f"statement -> {s}")

    def __repr__(self) -> str:
        """
        This method is responsible for the printing of the tokens that are returned by the get_tokens method.
        it takes no arguments and returns a string of the tokens. it basically overites the default __repr__ method."""
        for s in self._tokens:
            print(f"statement -> {s}")

    def performSentenceSplit(self, text):
        """This function takes part in tokenization of whole text blocks to aid the word tokenizer to be able to identifty tokens 
        based on specific word. This is a part which makes the whole system modular making it possible for the sentence to be handled as 
        blocks. this will also give the possibility to thet count of the number of sentences in 
        """
        formatter = re.compile(self._sentence_pattern, re.M)
        return formatter.findall(text)

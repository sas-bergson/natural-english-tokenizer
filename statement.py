
import os
import re

"""! @brief Example Python program with Doxygen style comments."""


class statement_tokenizer:
    def __init__(self):
        """
        This method is the constructor. where all the regex are defined and the word that the user or the calling file will use to call the method."""
        self._pattern = 'r"[A-Z]+[a-z]*\s\."'
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

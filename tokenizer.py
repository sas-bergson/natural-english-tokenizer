import json
from statement import statement_tokenizer


class QTokenizer(statement_tokenizer):
    """Tokenizes all english words that start with Q"""
    
    def __init__(self, text:str) -> None:
        super().__init__()
        self.__tokens = {
            "nouns":[], 
            "pronouns":[], 
            "verbs":[],
            "artcles":[],
            "adjectives":[],
            "adverbs":[],
            "prepositions":[],
            "conjunctions":[],
            "interjections":[]
        }

    def get_listed_tokens(self) ->  dict:
        """Returns a dictionary of tokens with the keys representing the nine 
        fundamental types of the english words and the values being a list of such words found in the _tokens property"""

        return self.__tokens

    def get_tokens_with_number(self)->dict:
        """Returns a dictionary of tokens with the keys representing the nine 
        fundamental types of the english words and the values being a total number of such words found in the _tokens property"""
        return {
            key:len(value)
            for key, value in self.__tokens.items()
        }

    @staticmethod
    def __load_data() -> dict:
        """with open()"""


open("data/DQ.json")
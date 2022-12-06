from statement import Statement_Tokenizer
from data import Dict_Data


class KTokenizer(Statement_Tokenizer):
    """Tokenizes all english words that start with K"""
    
    def __init__(self, text:str) -> None:
        super().__init__(text)
        ref = Dict_Data("K")
        self.__ref = ref.data
        self.__tokens = {
            "noun":[], 
            "pronoun":[], 
            "verb":[],
            "article":[],
            "adjective":[],
            "adverb":[],
            "preposition":[],
            "conjunction":[],
            "interjection":[],
            "no_match":[]
        }
        self.__parse_words()

    
    def __parse_words(self):
        """This method will be called at the appropria moment at run time"""
        words = list(filter(lambda w: w.startswith("K"), self.words))
        for word in words:
            for key, value in self.__ref.items():
                ## Need to emplement an algorithm that will best determine the type of the
                ## within the context of the sentence
                if word in value:
                    self.__tokens[key].append(word)
                    break
            else:
                self.__tokens["no_match"].append(word)

    

    def get_listed_tokens(self) ->  dict:
        """It just returns a dictionary of tokens with the keys representing the nine 
        fundamental types of the english words and the values being a list of such words found in 
        the _tokens property."""

        return  self.__tokens

    def get_tokens_with_number(self)->dict:
        """It just turns a dictionary of tokens with the keys representing the nine 
        fundamental types of the english words and the values being a total number of such words found in the 
        _tokens property."""

        return {key : len(value)  for key, value in self.__tokens.items()
        }

    def get_total_word(self) -> int:
        return sum(self.get_tokens_with_number().values())

    def __str__(self) -> str:
        return super().__str__()

if __name__ == "__main__":
    q_t = KTokenizer("""Gedeon got kidnapped by a kidnapper the day he knew he was going to have millions from his knowledge and was told to kneel """)
    print(q_t)
    print(q_t.get_listed_tokens())
    print(q_t.get_tokens_with_number())
    print("Total words: ", q_t.get_total_word())

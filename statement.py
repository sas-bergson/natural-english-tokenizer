import re

class Statement_Tokenizer:
    """!This is the base class of tokenization system. """
    
    def __init__(self, text:str) -> None:
        """!
        It abstracts the details of splitting the given text into tokens and let the client
        worry only about the results as she or he can get them though the statements property or words property.
        @param str text : it is the gevin text on which the the class operates and yield the result to the client.
        """
        self.__statement_pattern = '[\.!?]'
        self.__word_regex = re.compile('[^a-zA-Z]')
        self.__words = []
        text = re.sub(r"\s+", " ", text)
        self._get_tokens(text)
        
    def _get_tokens(self, text:str) -> None:
        """!This method Would be called at the appropriate moment at run time. It will split the given text in 
        statements and then in words so as to make the words available for the child classes that are going 
        to parse them.
        @param str text : it is the gevin text on which the the method operates."""

        if not text.strip():
            return
        self.__statements = re.split(self.__statement_pattern, text)
        if not self.__statements[-1]:
            self.__statements.pop()
        for statement in self.__statements:
            self.__words.extend(
                [self.__word_regex.sub("", word.upper()) for word in statement.split(" ") if word.strip()]
            )
    @property
    def statements(self):
        """Returns a list of the statements derived from the inputed text."""

        return self.__statements

    @property
    def words(self):
        "Returns a list of single words that can easily be further prossessed."
        return self.__words
    
    def __str__(self) -> str:
       repr = [f"statement {n} -> {s}" for n, s in enumerate(self.__statements, 1)]
       return "\n".join(repr)


if __name__ == "__main__":
    """! @test"""
    s_t = Statement_Tokenizer("Qatar 2022. I went, to be : qualified. Question? not Question")
    print(s_t.statements)
    print(s_t.words)
    print(s_t)

import re

"""! @brief Example Python program with Doxygen style comments."""


class statement_tokenizer:
    def __init__(self):
        """
        This method is the constructor. where all the regex are defined and the word that the user or the calling file will use to call the method."""
        self._pattern = r"[A-Z]+[a-z]*\s\."
        self._sentence_pattern = r'([A-Z][^\.!?]*[\.!?])'
        self._word_pattern = r'\w+'
        self._regex = re.compile(self._sentence_pattern)
        self._tokens = []

    def get_tokens(self, text) -> list:
        """
        This method is responsible for the splitting of the individual strings into the required tokens which
        take text (string) the text that is to be split into tokens. and returns a list of tokens."""
        self._tokens = self.peformSentenceSplit(text)
        return self._tokens

    def __str__(self) -> str:
        """
        This method is responsible for the printing of the tokens that are returned by the get_tokens method.
        it takes no arguments and returns a string of the tokens. it basically overrides the default __str__ method."""
        for s in self._tokens:
            print(f"statement -> {s}")

    def __repr__(self) -> str:
        """
        This method is responsible for the printing of the tokens that are returned by the get_tokens method.
        it takes no arguments and returns a string of the tokens. it basically overites the default __repr__ method."""
        for s in self._tokens:
            print(f"statement -> {s}")

    def peformSentenceSplit(self, text):
        """This function takes part in tokenization of whole text blocks to aid the word tokenizer to be able to identifty tokens 
        based on specific word. This is a part which makes the whole system modular making it possible for the sentence to be handled as 
        blocks. this will also give the possibility to thet count of the number of sentences in 
        """
        formatter = re.compile(self._sentence_pattern, re.M)
        return formatter.findall(text)

    def performWordSplit(self, text):
        """This function takes part in tokenization of whole text blocks to aid the word tokenizer to be able to identifty tokens 
        based on specific word. This is a part which makes the whole system modular making it possible for the sentence to be handled as 
        blocks. this will also give the possibility to thet count of the number of sentences in 
        """
        formatter = re.compile(self._word_pattern, re.M)
        return formatter.findall(text)

    def getAllTokens(self, text):
        """
        This function is responsible for the tokenization of the whole text block. it takes the text block as an argument and returns a list of tokens.
        """
        textData = self.retainAllTokens(text)
        return textData.split()

    def retainAllTokens(self, text):
        """
        this fuction is tp prevent the elimination of special characters to avoid elimination during text splitting 
        this will be especially important what there will to be identification of known patters.
        The function contains a special regular expresssion that checks all characaters individually
        """
        new_text = ""
        for i in range(len(text)):
            if re.match(r'\.|,|\?|\'|\)|\}|\]|\:|\;', text[i]):
                new_text = new_text+" "+text[i]
            elif re.match(r'\(|\{|\[|\s', text[i]):
                new_text = new_text+text[i]+" "
            else:
                new_text = new_text+text[i]
        return new_text
#    generate a dunction to match all words starting with an A or a

    def matchAllWordsStartingWithA(self, text):
        """The aim of this function is to match all words starting with an A or a this is performed by the use of a regular expression"""
        return re.findall(r'\b[Aa]\w+', text)

    def fsa(word):
        if(re.search(r'^a.+', word)):
            if re.search(r'.*ance$', word) or re.search(r'.*ence$', word) or re.search(r'.*ar$', word) or re.search(r'.*er$', word) or re.search(r'.*ir$', word) or re.search(r'.*or$', word) or re.search(r'.*ur$', word) or re.search(r'.*ism$', word) or re.search(r'.*ment$', word) or re.search(r'.*age$', word) or re.search(r'.*hood$', word) or re.search(r'.*ness$', word) or re.search(r'.*irt$', word) or re.search(r'.*er$', word) or re.search(r'.*bots', word):
                return "noun"
            elif re.search(r'.*able$', word) or re.search(r'.*ible$', word) or re.search(r'.*ant$', word) or re.search(r'.*ent$', word) or re.search(r'.*ists$', word) or re.search(r'.*ist$', word) or re.search(r'.*ous$', word) or re.search(r'.*ful$', word) or re.search(r'.*ish', word) or re.search(r'.*ive$', word) or re.search(r'.*ize$', word) or re.search(r'.*ate$', word) or re.search(r'.*ify$', word) or re.search(r'.*ise$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ize', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ize$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ize$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ize$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ize$', word) or re.search(r'.*ed$', word) or re.search(r'.*ate$', word) or re.search(r'.*y$', word) or re.search(r'.*ons$', word) or re.search(r'.*ing', word) or re.search(r'.*de', word) or re.search(r'.*ound', word):
                return "verb"
            elif re.search(r'.*ly$', word) or re.search(r'.*ry$', word) or word == "right" or re.search(r'.*here$', word) or word == "wrong" or re.search(r'.*here$', word) or word == 'soon' or re.search(r'.*soon$', word) or re.search(r'.*times$', word) or re.search(r'.*in$', word):
                return "adverb"
            else:
                return "valid but unknown"
        else:
            return "invalid word"
    # generate a function to identify all parts of speech in a text
    # def identifyAllPartsOfSpeech(self, text):


# if __name__ == "__main__":
#     data = statement_tokenizer()
#     text = """Today, technology is a subject of debate because it is considered to be a double-edged sword. While it has helped humanity in extending its potential with outstanding inventions, it is nonetheless threatening humankind through some other destructive ones. In addition to polluting the earth in unprecedented ways, wars have become more and more devastating due to technological inventions. Ethical dimensions of recent technological developments, such as DNA engineering, have become a focal point of questioning and discussion. Philosophical debates have arisen over the use of technology, with disagreements over whether technology improves the human condition or worsens it.
# To make matters worse, a consensus definition of technology has become more difficult to find due to recent evolution in science and its applications. It is especially confusing to decide whether technology refers to the machines (or more precisely the hardware), the rules that govern or make them work, the system that operates them or the different applications of science that are related to them. What is sure is that technology has shaped societies and adapted itself to people's changing needs.
# """
#     formatted = data.retainAllTokens(text.strip())
#     print(" ".join(data.matchAllWordsStartingWithA(formatted)))

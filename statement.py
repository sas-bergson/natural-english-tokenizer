import re
from parts_speech import *

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
        takes  text (string) the text that is to be split into tokens. and returns a list of tokens."""
        self._tokens = self.peformSentenceSplit(text)
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

    def matchAllWordsStartingWithB(self, text):
        """The aim of this function is to match all words starting with an A or a this is performed by the use of a regular expression"""
        data = re.findall(r'\b[Bb]\w+', text)
        print(data)
        return data

    def identifyPartsOfSpeech(self, text):
        """This function is responsible for the identification of the parts of speech of the words in the text block. 
        it takes the list of words as an argument and returns a list of parts of speech."""
        partsOfSpeech = []
        for word in text:
            if word in nouns:
                partsOfSpeech.append(word+" Noun")
            elif word in pronouns:
                partsOfSpeech.append(word+" Pronoun")
            elif word in adjectives:
                partsOfSpeech.append(word+" Adjective")
            elif word in verbs:
                partsOfSpeech.append(word+" Verb")
            elif word in adverbs:
                partsOfSpeech.append(word+" Adverb")
            elif word in conjunctions:
                partsOfSpeech.append(word+" Conjunction")
            elif word in interjections:
                partsOfSpeech.append(word+" Interjection")
            else:
                partsOfSpeech.append(word+" Unknown")
        return partsOfSpeech

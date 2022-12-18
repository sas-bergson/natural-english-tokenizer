import string

#Create Tokenizer Class

class Tokenizer():
    """
    The Tokenizer is a simple way of tokenizing. It is based on whitespaces and hyphens and uses a special token for splitting.
    It also does some processing to separate punctuation marks from words.
    Attributes
    ----------
    raw : str
        The raw text string passed as input to be tokenized.
    tokens : list of str
        The list of tokens after tokenization.
    """
    def __init__(self, sentence, token_boundries = ['', '-'], punctuations = string.punctuation, delimeter_token = '<SPLIT>'):
        """
        Parameters
        ----------
        input_text : str
            Text to be tokenized. Initialization immediately tokenizes the input text based on the input parameters.
        token_boundaries : list of str, optional
            List of characters to use as token splitters. Default to whitespaces and hyphens.
        punctuation: str or list of str, optional
            Punctuation characters used for preprocessing punctuation marks from words. Defaults to string library punctuation attribute.
        delimiter_token : str, optional
            Token to be used to split text. Defaults to '<SPLIT>'. Can be changed if the token word is reserved.
        """
        self.tokens = []
        self.raw = str(sentence)
        self._token_boundries = token_boundries
        self._delimeter_token = delimeter_token
        self._punctuations = punctuations
        self.index = 0
        self._tokenize()
    def _tokenize(self):
        work_sentence = self.raw
        
        for punctuation in self._puntuations:
            work_sentence = work_sentence.replace(punctuation, " " + punctuation + " ")
        
        for delimeter in self._token_boundries:
            work_sentence = work_sentence.replace(delimeter, self._delimeter_token)
        self.tokens = [x.strip() for x in work_sentence.split(self._delimeter_token) if x != '']
        
    def __iter_(self):
        return self

    def __next__(self):
        if self._index < len(self.tokens):
            result = self.tokens[self._index]
            self._index+=1
            return result
        raise StopIteration
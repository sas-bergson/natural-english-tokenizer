import sys, re

DEFAULT_SENTENCE_BOUNDARIES = ['(?<=[0-9]|[^0-9.])(\.)(?=[^0-9.]|[^0-9.]|[\s]|$)','\.{2,}','\!+','\:+','\?+']
DEFAULT_PUNCTUATIONS = ['(?<=[0-9]|[^0-9.])(\.)(?=[^0-9.]|[^0-9.]|[\s]|$)','\.{2,}','\!+','\:+','\?+','\,+', r'\(|\)|\[|\]|\{|\}|\<|\>']

class Document():
   
    def __init__(self, document_text):
       

        self.raw = document_text
        #self.sentences = sentencize(self.raw)
        self._index = 0

    def __getitem__(self, key):
        return self.sentences[key]

    def __repr__(self):
        return self.raw

    def __str__(self):
        return self.raw

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self.sentences):
            result = self.sentences[self._index]
            self._index+=1
            return result
        raise StopIteration
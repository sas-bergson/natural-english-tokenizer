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
    
class Sentence():
      
    def __init__(self, start_position, end_position, raw_document_reference):
       
        self.start_pos = int(start_position)
        self.end_pos = int(end_position)
        self._document_string = raw_document_reference
        self.next_sentence = None
        self.previous_sentence = None
        #self.tokens = tokenize(self._document_string[self.start_pos:self.end_pos])
        self._index = 0

    def get(self):
        return self._document_string[self.start_pos:self.end_pos]

    def __getitem__(self, key):
        return self.tokens[key]

    def __repr__(self):
        return self.get()

    def __str__(self):
        return self.get()

    def __eq__(self, other):
        return self.get() == other

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self.tokens):
            result = self.tokens[self._index]
            self._index+=1
            return result
        raise StopIteration
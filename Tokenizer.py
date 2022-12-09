from normalizer import Normalizer

class Tokenizer():
    def __init__(self)->None:
        self._n =Normalizer.verify_sentence(self)
    def tokenizer(self)->list:
        self._tokens = self._n.split()
        # print(self._tokens)
        return self._tokens
t=Tokenizer()
t.tokenizer()
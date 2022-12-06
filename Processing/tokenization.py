
class DummySentencizer():
    
    def __init__(self, input_text, split_characters=['.','?','!',':'], delimiter_token='<SPLIT>'):

        self.sentences = []
        self.raw = str(input_text)
        self._split_characters=split_characters
        self._delimiter_token=delimiter_token
        self._index=0
        self._sentencize()
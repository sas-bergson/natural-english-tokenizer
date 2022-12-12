import re
import dictionary as dic


class StatementTokenizer:
    """!The statement tokenizer class.
    Tokenize a statement into nouns, adjectives, verbs and also into punctuation elements namely ',', '?','.'
    """

    def __init__(self):
        """!The StatementTokenizer class initializer."""

        self._stmt_pattern = re.compile(r'[\w*\s]*[\.|\?|,|;]? ?')
        self._token_pattern = re.compile(r'\w*|\s*|[\.|\?|,|;]')
        self._statements = []
        # Array of tokens
        self._tokens = []
        self.dictionary = dic.Dictionary('dictionary.txt')

    def get_statements(self, text) -> list:
        regex = re.compile(self._stmt_pattern)
        self._statements = regex.findall(text)
        for s in self._statements:
            if len(s) == 0:
                self._statements.remove(s)
        return self._statements

    def get_tokens(self, text) -> list:
        regex = re.compile(self._token_pattern)
        self._tokens = regex.findall(text)
        for t in self._tokens:
            if len(t) == 0:
                self._tokens.remove(t)
        return self._tokens

    def __str__(self) -> str:
        ret = ''
        for s in self._statements:
            ret += f"statement -> {s} (length = {len(s)})\n"
        for t in self._tokens:
            word = self.dictionary.find_word(t.lower())
            word_type = 'unknown type'
            if word:
                word_type = word['type']
            ret += f"token -> {t} (word type = {word_type}) (length = {len(t)})\n"
        return ret

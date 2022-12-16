import re
import dictionary as dic


class Tokenizer:
    """!The statement tokenizer class.
    Tokenize a statement into nouns, adjectives, verbs and also into punctuation elements namely ',', '?','.'
    """

    def __init__(self, input_expression: str):
        """!The Tokenizer class initializer."""

        self._stmt_pattern = re.compile(r'[\w*\s]*[\.|\?|,|;]? ?')
        self._token_pattern = re.compile(r'\w*|\s*|[\.|\?|,|;]')
        self._input_expression = input_expression
        self._statements = []
        # Array of tokens
        self._tokens = []
        self.dictionary = dic.Dictionary()

    def get_statements(self) -> list:
        regex = re.compile(self._stmt_pattern)
        self._statements = regex.findall(self._input_expression)
        for s in self._statements:
            if len(s) == 0:
                self._statements.remove(s)
        return self._statements

    def get_tokens(self) -> list:
        regex = re.compile(self._token_pattern)
        self._tokens = regex.findall(self._input_expression)

        def get_only_text(t):
            if not re.match(re.compile(r"\s"), t):
                return t

        self._tokens = filter(get_only_text, self._tokens)
        self._tokens = list(self._tokens)

        def set_type(value: str):
            word = self.dictionary.find_word(value.lower())
            word_type = 'word'
            if word:
                word_type = word['type']
            return {
                'type': word_type,
                'value': value
            }

        self._tokens = map(set_type, self._tokens)
        self._tokens = list(self._tokens)
        return self._tokens

    def __str__(self) -> str:
        ret = ''
        for s in self._statements:
            ret += f"statement -> {s} (length = {len(s)})\n"
        for t in self._tokens:
            ret += f"token -> {t['value']} (word type = {t['type']}) (length = {len(t['value'])})\n"
        return ret

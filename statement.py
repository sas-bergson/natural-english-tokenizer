import re


class Statement_Tokenizer:

    def __init__(self, text: str) -> None:

        self.__statement_pattern = '[\.!?]'
        self.__word_regex = re.compile('[^a-zA-Z]')
        self.__words = []
        text = re.sub(r"\s+", " ", text)
        self._get_tokens(text)

    def _get_tokens(self, text: str) -> None:

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

        return self.__statements

    @property
    def words(self):

        return self.__words

    def __str__(self) -> str:
        repr = [f"statement {n} -> {s}" for n, s in enumerate(self.__statements, 1)]
        return "\n".join(repr)


if __name__ == "__main__":
    """! @test"""
    s_t = Statement_Tokenizer("Hi my name is Moubarack")
    print(s_t.statements)
    print(s_t.words)
    print(s_t)

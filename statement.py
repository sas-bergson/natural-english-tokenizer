import os
import re


class StatementTokenizer:

    def __init__(self):
        self._statements_regex = re.compile(r"\.")
        self._noun_regex = re.compile(r"[a-zA-Z]")
        self._comma_regex = re.compile(r",")
        self._interrogation_point_regex = re.compile(r"\?")
        self._full_stop_regex = re.compile(r"\.")
        self._white_space_regex = re.compile(r"\s")
        self._tokens = []

    def get_statements(self, input_expression) -> list:
        return re.split(self._statements_regex, input_expression)

    def __str__(self) -> str:
        for s in self._tokens:
            print(f"statement -> {s}")

    @staticmethod
    def tokenize_pattern(input_type, pattern, input_expression, current):
        char = input_expression[current]
        consumed_chars = 0
        if re.match(pattern, char):
            value = ''
            while char and re.match(pattern, char):
                value += char
                consumed_chars += 1
                try:
                    char = input_expression[current + consumed_chars]
                except:
                    char = None

            return [consumed_chars, {'type': input_type, 'value': value}]
        return [0, None]

    def tokenize_noun(self, input_expression, current):
        return StatementTokenizer.tokenize_pattern("noun", self._noun_regex, input_expression, current)

    def tokenize_comma(self, input_expression, current):
        return StatementTokenizer.tokenize_pattern("comma", self._comma_regex, input_expression, current)

    def tokenize_interrogation_point(self, input_expression, current):
        return StatementTokenizer.tokenize_pattern("interrogation point", self._interrogation_point_regex,
                                                   input_expression, current)

    def tokenize_full_stop(self, input_expression, current):
        return StatementTokenizer.tokenize_pattern("full stop", self._full_stop_regex, input_expression, current)

    def skip_white_space(self, input_expression, current):
        if re.match(self._white_space_regex, input_expression[current]):
            return [1, None]
        else:
            return [0, None]

    @staticmethod
    def tokenize_sentence(input_expression, current):
        if re.match(re.compile(r"[A-Z]"), input_expression[current]):
            value = ''
            consumed_chars = 0
            char = input_expression[current + consumed_chars]
            while char != '.':
                if char is None:
                    raise Exception("Unterminated sentence")

                value += char
                consumed_chars += 1
                try:
                    char = input_expression[current + consumed_chars]
                except:
                    char = None
            if char == '.':
                value += char

            return [(consumed_chars + 1), {'type': 'sentence', 'value': value}]

        return [0, None]

    def get_sentences(self, statement):
        sentences = []
        current = 0
        # Load mini tokenizers
        tokenizers = [self.skip_white_space, StatementTokenizer.tokenize_sentence]

        while current < len(statement):
            tokenized = False
            # Loop in all mini tokenizers in order to categorize found tokens
            for function in tokenizers:
                if tokenized:
                    break
                result = function(statement, current)
                if result[0] != 0:
                    tokenized = True
                    current += result[0]
                if result[1]:
                    sentences.append(result[1]['value'])
        return sentences

    def tokenizer(self, statement):
        sentences = self.get_sentences(statement)
        for sentence in sentences:
            current = 0
            # Load mini tokenizers
            tokenizers = [self.skip_white_space, self.tokenize_noun, self.tokenize_comma, self.tokenize_interrogation_point, self.tokenize_full_stop]
            while current < len(sentence):
                tokenized = False
                char = sentence[current]
                # Loop in all mini tokenizers in order to categorize found tokens
                for function in tokenizers:
                    if tokenized:
                        break
                    result = function(sentence, current)
                    if result[0] != 0:
                        tokenized = True
                        current += result[0]
                    if result[1]:
                        self._tokens.append(result[1])

                # If not reach at the end of the sentence and unknown char
                if not tokenized:
                    raise Exception("I don't know what this character is: ", char)
                # If reach at the end of the sentence
                elif char == '.':
                    print('sentence : "', sentence, '" ', 'successfully tokenized')
        print('tokens:', self._tokens)

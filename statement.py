import json
import re


class StatementTokenizer:
    """!The statement tokenizer class.
    Tokenize a statement into nouns, adjectives, verbs and also into punctuation elements namely ',', '?','.'
    """

    def __init__(self):
        """!The StatementTokenizer class initializer."""

        # Regular expression for match string in a sentence
        self._string_regex = re.compile(r"[a-zA-Z][0-9]*")
        # Regular expression for match comma in a sentence
        self._comma_regex = re.compile(r",")
        # Regular expression for match interrogation point in a sentence
        self._interrogation_point_regex = re.compile(r"\?")
        # Regular expression for match full stop in a sentence
        self._full_stop_regex = re.compile(r"\.")
        # Regular expression for match white space
        self._white_space_regex = re.compile(r"\s")
        # Array of tokens
        self._tokens = []
       
        # Load dictionary which contains the 100 first words beginning with letter N 
        file = open('dictionary.json')
        json_data = json.load(file)
        print(type(json_data))
        self.dictionary = []
        for value in json_data:
            self.dictionary.append({
                'type': value['type'],
                'value': value['value']
            })
        # print(self.dictionary)
        file.close()

    def find_word(self, value: str) -> object:
        """! Find a word object from dictionary of words.
        @param value   The input value to use for the search.
        @return  The corresponding word object.
        """

        for x in self.dictionary:
            if x['value'] == value:
                return x

    def tokenize_pattern(self, word_type: str, pattern, expression: str, current: int) -> list:
        """! Find a word object from dictionary of words.
        @param word_type   The word type (if exists) to set.
        @param pattern   The pattern to use like regular expression to filter the input expression.
        @param expression   The input expression to tokenize.
        @param current   The current position in the loop of expression.
        @return  The array containing token.
        """

        char = expression[current]
        consumed_chars = 0
        if re.match(pattern, char):
            value = ''
            while char and re.match(pattern, char):
                value += char
                consumed_chars += 1
                try:
                    char = expression[current + consumed_chars]
                except:
                    char = None

            if word_type:
                return [consumed_chars, {'type': word_type, 'value': value}]
            else:
                word = self.find_word(value.lower())
                if word:
                    return [consumed_chars, {'type': word['type'], 'value': word['value']}]
                else:
                    return [consumed_chars, {'type': 'unknown type', 'value': value}]
        return [0, None]

    def tokenize_string(self, expression: str, current: int) -> list:
        """! Extract a string which match a given pattern.
        @param expression   The input expression to tokenize.
        @param current   The current position in the loop of expression.
        @return  The array containing token.
        """

        return self.tokenize_pattern(None, self._string_regex, expression, current)

    def tokenize_comma(self, expression: str, current: int) -> list:
        """! Extract a comma.
        @param expression   The input expression to tokenize.
        @param current   The current position in the loop of expression.
        @return  The array containing token.
        """

        return self.tokenize_pattern("comma", self._comma_regex, expression, current)

    def tokenize_interrogation_point(self, expression: str, current: int) -> list:
        """! Extract an interrogation point.
        @param expression   The input expression to tokenize.
        @param current   The current position in the loop of expression.
        @return  The array containing token.
        """

        return self.tokenize_pattern("interrogation point", self._interrogation_point_regex, expression, current)

    def tokenize_full_stop(self, expression: str, current: int) -> list:
        """! Extract a full stop.
        @param expression   The input expression to tokenize.
        @param current   The current position in the loop of expression.
        @return  The array containing token.
        """

        return self.tokenize_pattern("full stop", self._full_stop_regex, expression, current)

    def skip_white_space(self, expression: str, current: int) -> list:
        """! Check if current char is white space.
        @param expression   The input expression to tokenize.
        @param current   The current position in the loop of expression.
        @return  The array without token.
        """

        if re.match(self._white_space_regex, expression[current]):
            return [1, None]
        else:
            return [0, None]

    @staticmethod
    def tokenize_statement(expression: str, current: int) -> list:
        """! Extract a statement.
        @param expression   The input expression to tokenize.
        @param current   The current position in the loop of expression.
        @return  The array containing token.
        """

        # Check if expression begin with uppercase letter
        # if re.match(re.compile(r"[A-Z]"), expression[current]):
        value = ''
        consumed_chars = 0
        char = expression[current + consumed_chars]
        while char != ',' and char != '.':
            if char is None:
                raise Exception("Unterminated statement")

            value += char
            consumed_chars += 1
            try:
                char = expression[current + consumed_chars]
            except:
                char = None

        # If end of expression, add full stop at the end of token
        if char == ',' or char == '.':
            # print("char:", char, "value:", value)
            value += char

        return [(consumed_chars + 1), {'type': 'statement', 'value': value}]

        # return [0, None]

    def get_statements(self, statement: str) -> list[str]:
        """! Extract list of statements which composed the statement.
        @param statement   The input expression to tokenize.
        @return  The array of statements.
        """
        statements = []
        current = 0
        # Load mini tokenizers
        tokenizers = [self.skip_white_space, StatementTokenizer.tokenize_statement]

        while current < len(statement):
            tokenized = False
            # Loop in all mini tokenizers in order to get statements
            for function in tokenizers:
                if tokenized:
                    break
                result = function(statement, current)
                if result[0] != 0:
                    tokenized = True
                    current += result[0]
                if result[1]:
                    statements.append(result[1]['value'])
        return statements

    def tokenizer(self, text: str):
        """! Tokenizes statement.
        @param text   The input text to tokenize.
        """

        statements = self.get_statements(text)
        # Loop over the array of statements and tokenize each of them
        for statement in statements:
            current = 0
            # Load mini tokenizers
            tokenizers = [self.skip_white_space, self.tokenize_string, self.tokenize_comma,
                          self.tokenize_interrogation_point, self.tokenize_full_stop]
            while current < len(statement):
                tokenized = False
                char = statement[current]
                # Loop in all mini tokenizers in order to categorize found tokens
                for function in tokenizers:
                    if tokenized:
                        break
                    result = function(statement, current)
                    if result[0] != 0:
                        tokenized = True
                        current += result[0]
                    if result[1]:
                        self._tokens.append(result[1])

                # If not reach at the end of the statement and unknown char
                if not tokenized:
                    raise Exception("I don't know what this character is: ", char)
                # If reach at the end of the statement
                elif char == ',' or char == '.':
                    print('statement : "', statement, '" ', "(length = ", len(statement), ")", 'successfully tokenized')
        for token in self._tokens:
            print('token -> ', token['value'], "(length = ", len(token['value']), ")")

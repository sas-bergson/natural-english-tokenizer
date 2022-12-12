

class Dictionary:

    def __init__(self, dictionary_file):
        """!The StatementTokenizer class initializer."""

        # Load dictionary words from 'dictionary.txt' file which contains the 100 first words in natural english
        # language
        file = open(dictionary_file, 'r')
        lines = file.readlines()
        count = 0
        self.dictionary = []
        for line in lines:
            count += 1
            values = line.strip().split(',')
            self.dictionary.append({
                'type': values[1],
                'value': values[0]
            })

    def find_word(self, value: str) -> object:
        """! Find a word object from dictionary of words.
        @param value   The input value to use for the search.
        @return  The corresponding word object.
        """

        for x in self.dictionary:
            if x['value'] == value:
                return x



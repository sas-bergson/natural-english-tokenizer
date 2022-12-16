

class Conjunction:

    def __init__(self):
        """!The Conjunction class initializer."""

        # Load conjunctions from 'conjunctions.txt' file
        file = open('conjunctions.txt', 'r')
        lines = file.readlines()
        count = 0
        self.conjunctions = []
        for line in lines:
            count += 1
            values = line.strip().split(',')
            self.conjunctions.append({
                'type': values[1],
                'value': values[0]
            })

    def find_word(self, value: str) -> object:
        """! Find a word object from conjunctions list.
        @param value   The input value to use for the search.
        @return  The corresponding word object or None if nothing found.
        """

        for x in self.conjunctions:
            if x['value'] == value:
                return x


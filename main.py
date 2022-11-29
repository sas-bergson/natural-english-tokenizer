import re
from errors import *
# class RegexPatterns: 
#     _phrase_punctuation = ['.', '?', '...', '!']
#     # _phrase = re.compile(r"^[A-Z]+[a-z]*\s?\.$")
#     _phrase_start = re.compile(r"^[A-Z]")
#     _phrase_end = re.compile(r"\.$")
#     _space = re.compile(r"\s")


class StatementTokenizer:
    """
        Arguments
        ----------
            text(str): The sentence to work with

        ... 

        methods
        -------
        validate_phase()
            Checks if the sentence starts with a capital letter and ends with a punctuation

        tokenize()
            Checks if word of in sentence is in wordlist.

        remove_punc()
            Removes punctuation at the end of the sentence

        run()
            Removes punctuation at the end of the sentence
        

    """
    def __init__(self, text):
        """
            Arguments
            ----------
                text(str): The sentence to work with

            ... 
            
            methods
            -------
            validate_phase()
                Checks if the sentence starts with a capital letter and ends with a punctuation

            tokenize()
                Checks if word of in sentence is in wordlist.

            remove_punc()
                Removes punctuation at the end of the sentence

            run()
                Removes punctuation at the end of the sentence
        

        """
        self.sentence = text
        self._types = []
        self._phrase_punctuation = ('.', '?', '...', '!')
        # self._phrase = re.compile(r"^[A-Z]+[a-z]*\s?\.$")
        self._phrase_start = re.compile(r"^[A-Z]")
        self._phrase_end = re.compile(r"\.$")
        self._space = re.compile(r"\s")

    def validate_phrase(self):
        """ Checks if the sentence starts with a capital letter and ends with a punctuation """
        if re.match(self._phrase_start, self.sentence):
            if self.sentence.endswith(self._phrase_punctuation):
                return True
            else:
                raise PhraseEndError("Invalid sentence. A sentence must end with a punctuation mark")
        else:
            raise PhraseStartError("Invalid sentence. A sentence must start with a capital letter")

    def tokenize(self, word):
        """ 
            Checks if word of in sentence is in wordlist. 
            Args: 
                word(str): word in a sentence
        """
        word_type = "unknown"
        with open("./wordlist2.txt", "r") as wordlist: 
            for line in wordlist: 
                if len(line) > 4: 
                    try:
                        line_word, line_type = line.strip().split()
                    except ValueError:
                        line_type = word_type
                    finally:
                        if line_word.lower() == word.lower(): 
                            word_type = line_type

        self._types.append(word_type)

    def split_sentences(self):
        return self.sentence.split(".")

    def remove_punc(self):
        """ 
            Removes punctuation at the end of the sentence 
        
            Attributes
            ----------

            Returns
            --------
            returns a list
        
        
        """
        words = self.sentence.strip().split()
        for punc in self._phrase_punctuation:
            if punc in words[-1]:
                if words[-1].endswith(self._phrase_punctuation[2]):
                    words[-1] = words[:-3]
                else:
                    words[-1] = words[-1][:-1]
        return words
    
    def run(self):
        """ The main function to launch """
        if self.validate_phrase():
            words = self.remove_punc()
            for word in words:
                self.tokenize(word)

        print("Results: ")
        print("=========================================================================")
        print(f'"{self.sentence}"')
        print(self._types)
        print("=========================================================================")


if __name__ == '__main__':
    sentence = "Xian phrase xenia now xes needing many word."
    st = StatementTokenizer(sentence)
    st.run()


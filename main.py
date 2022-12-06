import re
from errors import *
# class RegexPatterns: 
#     _phrase_punctuation = ['.', '?', '...', '!']
#     # _phrase = re.compile(r"^[A-Z]+[a-z]*\s?\.$")
#     _phrase_start = re.compile(r"^[A-Z]")
#     _phrase_end = re.compile(r"\.$")
#     _space = re.compile(r"\s")


class StatementTokenizer:
    def __init__(self, text):
        self.sentence = text
        # self._types = []
        self.results = {}
        self.counter = 0
        self._phrase_punctuation = ('.', '?', '...', '!')
        # self._phrase = re.compile(r"^[A-Z]+[a-z]*\s?\.$")
        self._phrase_start = re.compile(r"^[A-Z]")
        self._phrase_end = re.compile(r"\.$")
        self._space = re.compile(r"\s")
        self.sentences = self.split_sentences()

    def split_sentences(self, sep=".")-> list:
        """ Split sentences and return a list of all sentences
        verifies that every element of the returned list is not empty"""
        splitting = self.sentence.split(sep)
        results = []
        index = 0
        for x in splitting:
            if x: 
                x += sep
            results.append(x.strip())
            index +=1

        sentence_index = 0
        for sentence in results:
            if not sentence: 
                results.remove(sentence)
            sentence_index +=1
        return results

    def validate_phrase(self, sentence)-> bool:
        """ Checks if the sentence starts with a capital letter and ends with a punctuation """
        # for sentence in self.sentences:
        if re.match(self._phrase_start, sentence):
            if sentence.endswith(self._phrase_punctuation):
                return True
            else:
                raise PhraseEndError(f"Invalid sentence. A sentence must end with a punctuation mark\n{sentence}")
        else:
            raise PhraseStartError(f"Invalid sentence. A sentence must start with a capital letter\n{sentence}")

    def tokenize(self, word):
        word_type = "unknown"
        if word in self._phrase_punctuation:
            word_type = "punctuation"
            # self._types.append(word_type)
            self.results_to_dic(word, word_type)
            return True
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
                            self.counter +=1

        # self._types.append(word_type)
        self.results_to_dic(word, word_type)            

    def remove_punc(self, sentence)-> str:
        words = sentence.strip().split()
        for punc in self._phrase_punctuation:
            if punc in words[-1]:
                if words[-1].endswith(self._phrase_punctuation[2]):
                    words[-1] = words[:-3]
                else:
                    words[-1] = words[-1][:-1]
        return words
    
    def results_to_dic(self, word, word_type):
        self.results.update({word.lower(): word_type})

    @staticmethod
    def counter_words(results)-> int:
        _counter = 0
        for k, v in results.items():
            if not (v == "unknown" or v == "punctuation"):
                _counter += 1
        return _counter
    
    def run(self):
        """ The main function to launch """
        for sentence in self.sentences:
            words = self.remove_punc(sentence) # remove punctuation at the end
            for word in words: # get every word in the sentence
                self.tokenize(word)

        # if self.validate_phrase():
        #     for sentence in self.sentences:
        #         words = self.remove_punc(sentence)
        #         for word in words:
        #             self.tokenize(word)

        print("Results: ") 
        print(f"Number of words of the selected letter found: {self.counter_words(self.results)}") 
        print(f"Number of times words of the selected letter found: {self.counter}") 

        print("=========================================================================")
        print(f'"{self.sentence}"')
        print(self.results)
        print("=========================================================================")

if __name__ == '__main__':
    sentence = "Xian phrase xenia now xes needing many word. This is the xenia second phrase!"
    st = StatementTokenizer(sentence)
    st.run()


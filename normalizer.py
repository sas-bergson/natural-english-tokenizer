import re

class Normalizer():
    def verify_sentence(self)->str:
        # regex=re.compile("(^[A-Z]+[a-z\s]+\.$)+")
        self._regex=re.compile("^[A-Za-z\.\,\?\!\s]+$")
        try:
            self._compiled_text=self._regex.search("This is a test designed to verify the behaviour\
            of the tokenizer. If it succeeds, we will move to the design of a file scanner.")[0]
            # print(self._compiled_text)
            return self._compiled_text
        except:
            print("sentence not matching regex expression")
n=Normalizer()
n.verify_sentence()



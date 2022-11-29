import re


class StatementTokenizer:
    

    def __init__(self):
       

        
        self._noun_regex = re.compile(r"[a-zA-Z][0-9]*")
       
        self._comma_regex = re.compile(r",")
        
        self._interrogation_point_regex = re.compile(r"\?")
      
        self._full_stop_regex = re.compile(r"\.")
        
        self._white_space_regex = re.compile(r"\s")
        
        self._tokens = []
       
        file = open('dictionary.txt', 'r')
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

   

    def tokenize_string(self, expression: str, current: int) -> list:
       

        return self.tokenize_pattern(None, self._noun_regex, expression, current)

    def tokenize_comma(self, expression: str, current: int) -> list:
        
        return self.tokenize_pattern("comma", self._comma_regex, expression, current)

    def tokenize_interrogation_point(self, expression: str, current: int) -> list:
       

        return self.tokenize_pattern("interrogation point", self._interrogation_point_regex, expression, current)

    def tokenize_full_stop(self, expression: str, current: int) -> list:
        

        return self.tokenize_pattern("full stop", self._full_stop_regex, expression, current)

    def skip_white_space(self, expression: str, current: int) -> list:
      

        if re.match(self._white_space_regex, expression[current]):
            return [1, None]
        else:
            return [0, None]

   

    def get_sentences(self, statement: str) -> list[str]:
     
        sentences = []
        current = 0
     
        tokenizers = [self.skip_white_space, StatementTokenizer.tokenize_sentence]

        while current < len(statement):
            tokenized = False
            
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

    def tokenizer(self, statement: str):
        

        sentences = self.get_sentences(statement)
       
        for sentence in sentences:
            current = 0
            
            tokenizers = [self.skip_white_space, self.tokenize_string, self.tokenize_comma,
                          self.tokenize_interrogation_point, self.tokenize_full_stop]
            while current < len(sentence):
                tokenized = False
                char = sentence[current]
               
                for function in tokenizers:
                    if tokenized:
                        break
                    result = function(sentence, current)
                    if result[0] != 0:
                        tokenized = True
                        current += result[0]
                    if result[1]:
                        self._tokens.append(result[1])

               
                if not tokenized:
                    raise Exception("I don't know what this character is: ", char)
               
                elif char == '.':
                    print('sentence : "', sentence, '" ', 'successfully tokenized')
        print('tokens:', self._tokens)

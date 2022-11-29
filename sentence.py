
import regex as re

class Sentence:
    
    f = open('./assets/sample.txt', 'r')
    sample = f.read()
    f.close()
    
    def sentence_check(text):
        pattern = re.compile('[A-Z][^\.!?]*[!?\.]')
        if re.match(pattern, text):
            text
            print(text)
            return text
        else:
            print("Invalid")
        
    
    sentence_check(sample)
    
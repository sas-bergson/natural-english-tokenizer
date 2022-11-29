
import regex as re

class Sentence:
    
    f = open('./assets/sample.txt', 'r')
    sample = f.read()
    f.close()
    
    def sentence_check(text):
        '''This function checks if the text is a proper sentence'''
        
        pattern = re.compile('[A-Z][^\.!?]*[!?\.]')  
        if re.match(pattern, text):
            checked_text = text
            print(checked_text)
            return checked_text
        else:
            print("Invalid")
        
    def get_token(text) -> list :
        '''This functions splits the sentence into words'''
        tokens = re.split(r'\s+', text)
        return tokens
        
        
    sentence_check(sample)
    get_token(sample)
    
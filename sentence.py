
import regex as re

class Sentence:
    
    f = open('./assets/sample.txt', 'r')
    sample = f.read()
    f.close()
    
    def sentence_check(text):
        '''This function checks if the text is a proper sentence'''
        
        pattern = re.compile('[A-Z][^\.!?]*[!?\.]',re.M)  
        if re.match(pattern, text):
            checked_text = text
            print(checked_text)
            return checked_text
        else:
            print("Invalid")
        
    def get_token(text) -> list :
        '''This functions splits the sentence into words'''
        tokens = re.split(r'\s+', text)
        print(tokens)
        return tokens
    
    def words_withV(text):
        '''Matching words that begin with V and printing them'''
        v_pattern = re.compile(r'\b[v]\w+', re.I)
        x = re.findall(v_pattern, text)
        print(x)
    def matchtextlength(text):
        '''This function returns the length of all the words in this sentence'''
        l_pattern = re.compile(r'([a-zA-Z0-9]+)')
        # sentence_split = re.split('\s', text)
        # print(sentence_split)
        length = len(re.findall(l_pattern, text))
        print(length)
        return length
        
    sentence_check(sample)
    get_token(sample)
    words_withV(sample)
    matchtextlength(sample)
    
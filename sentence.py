
import regex as re

class Sentence:
    
    def __init__(self):
        self._sentence_pattern = r'[A-Z][^\.!?]*[!?\.]'
        self._v_pattern = re.compile(r'\b[v]\w+', re.I)
        self._space_split = r'\s+'
        self._pattern = r'[!,\.?]\B'
        self.l_pattern = re.compile(r'([a-zA-Z0-9])')
        self.word_pattern = re.compile(r'[a-zA-Z0-9]+')
        self._adverbs = r"\w+ly\b"
        self._verbs = r"\w+ing\b"
    
    def sentence_check(self, text):
        '''This function checks if the text is a proper sentence'''
        
        checked = re.findall(self._sentence_pattern, text)
        for word in checked:
            print(word)
        # print(checked)
        return word
        
    def get_token(self, text) -> list :
        '''This functions splits the sentence into words'''
        
        # tokens = re.split(self._pattern, text)
        tokens = text.split('.')
        
        for word in tokens:
            print(word)
        # print(tokens)
        return tokens
    
    def words_withV(self, text):
        '''Matching words that begin with V and printing them'''
        
        x = re.findall(self._v_pattern, text)
        print(x)
        
    def matchtextlength(self, text):
        '''This function returns the length of all the words in this sentence'''
        
        for x in range(len(text)):
            print("".join([" ".join(text[x]), " (length = ", str(len(text[x])), ")"] ))
            # print(len(text[x]))
            
        # words = re.findall(self.word_pattern, text)
        # length = len(re.findall(self.l_pattern, text))
        
        # print("".join([" ".join(words),"   (length = ", str(length), ")"]))
        # return length

    def findalladverbs(self, text):
        '''This functions displays all the adverbs in a text and their position'''
        
        for m in re.finditer(self._adverbs, text):
            print('Adverb: '+'%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
    
    def findallverbs(self, text):
        '''This functions displays all the adverbs in a text and their position'''
        
        for m in re.finditer(self._verbs, text):
            print( 'verb:'+'%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
   
    
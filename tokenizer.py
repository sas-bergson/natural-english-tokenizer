import regex as re
from sentence import Sentence

if __name__ =="__main__":
    f = open('./assets/sample.txt', 'r')
    sample = f.read()
    f.close()
    
    tokenizer = Sentence()
    
    tokenizer.sentence_check(sample)
    # tokenizer.words_withV(sample)
    tokenizer.get_token(sample)
    # tokenizer.matchtextlength(sample)
    # tokenizer.findalladverbs(sample)
    # tokenizer.findallverbs(sample)
    
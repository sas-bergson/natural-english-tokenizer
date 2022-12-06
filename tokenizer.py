import regex as re
from sentence import Sentence

if __name__ =="__main__":
    f = open('./assets/sample.txt', 'r')
    sample = f.read()
    f.close()
    
    sampletext= '''Do not voilate rules rather value the various varieties of verbs. quickly and running.
A set of words that is complete in itself, typically containing a subject and predicate?'''
    
    text = 'This is a test designed to verify the behaviour of the tokenizer. If it succeeds, we will move to the design of a file scanner.'
    
    tokenizer = Sentence()
    
    sentence_processing = tokenizer.sentence_check(text)
    print('=======================')
    print('This are the words that start with v: ')
    tokenizer.words_withV(text)
    print('=======================')
    tokenized_words = tokenizer.get_token(text)
    print('=======================')
    tokenizer.matchtextlength(tokenized_words)
    print('=======================')
    tokenizer.findalladverbs(text)
    print('=======================')
    tokenizer.findallverbs(text)
    
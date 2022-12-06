from statement import statement_tokenizer

test = statement_tokenizer()
        
def main():
    text = 'This is a test designed to verify the behaviour\
        of the tokenizer. If it succeeds, we will move to the design of a file scanner.'
    test.get_sentence(text)
    
    test.list_sentences()
    print("")
    
    test.get_tokens(text)
    print("")
    
    test.get_token_number()
    print("")
    
    test.__str__()
    print("")
    
    test.identify_tokens()
    
main() 


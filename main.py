from statement import statement_tokenizer

test = statement_tokenizer()
        
def main():
    test.get_sentence("Hi my name is Yan, student at the ICT University.  I love compiler construction.")
    
    test.list_sentences()
    print("")
    
    test.get_tokens()
    print("")
    
    test.get_token_number()
    print("")
    
    test.__str__()
    print("")
    
    test.identify_tokens()
    
main() 

from statement import statement_tokenizer

test = statement_tokenizer()
        
def main():
    test.get_sentence("Hi my name is Yan, student at the ICT University.  I love compiler construction.")
    test.list_sentences()
    test.get_tokens()
    test.__str__()
    test.tokenize_tokens()
    
main() 

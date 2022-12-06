import token 

Test = token.tokenizer()

text = 'I beleive in Christ. The choir is made up of youths, parents, and grandparents. The fear of the Lord is my salvation.'

test = Test.sentence_split(text)
test_paragraph = Test.word_split(test)
print(test_paragraph)
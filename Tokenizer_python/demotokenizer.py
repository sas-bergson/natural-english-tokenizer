import tokenizer 

Test = tokenizer.tokenizer()

text = 'This is a test designed to verify the behaviour of the tokenizer. If it succeeds, we will move to the design of a file scanner.'
test = Test.sentence_split(text)
test_paragraph = Test.word_split(test)
print(test_paragraph)
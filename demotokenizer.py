import token 

text = 'I beleive in Christ. The choir is made up of youths, parents, and grandparents. The fear of the Lord is my salvation.'
test = token.sentence_split(text)
test_paragraph = token.word_split(test)
print(test_paragraph)
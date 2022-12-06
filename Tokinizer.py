# This function splits a paragraph into sentences and stores them as a list
# which it then returns a list of sentences.
def sentence_split(text):
    sentences = text.split('.')
    count = 0

    # This function removes the empty values from the list.
    sentences.remove('')
    print('sentences(' + str(len(sentences)) + ') : ')
    for sentence in sentences:
        if (sentence != ''):
            print(' -> ' + sentence)
            sentence.split(',')
        else:
            sentences.remove(sentence)
    return sentences


# This function splits sentences into words and stores them as a list.
def word_split(text):
    sentences_list = []
    for sentence in text:
        words = sentence.split(' ')
        if (words.count('') >= 1):
            words.remove('')
        print('Sentence' + ':\n' + sentence)
        print('Words:' + '(' + str(len(words)) + ')')
        for word in words:
            # Removing Commas from words
            # if (word.count(',')>=1):
            #   word.remove(',')
            print('-> ' + word)
        sentences_list.append(words)
    return sentences_list


text = '. My name is Penn Roy Ndah, I school at the ICT University. I study software engineering.'
test = sentence_split(text)
box = word_split(test)
print(box)


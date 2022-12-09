
class tokenizer: 
    #This function splits a paragraph into sentences and stores them as a list
    # which it then returns as a list of sentences.
    def sentence_split(self, text):

        #splits text into sentences
        sentences = text.split('.')
        count = 0

        # sentences.remove('') #This line removes the empty values from the list.
        print('\nTokenizer:\n'+text)
        print('sentences('+str(len(sentences))+') : ')
        for sentence in sentences:
            sentence += '.'
            if (sentence != ''):
                print(' -> '+sentence)
            else:
                sentences.remove(sentence)
            sub_sentence = sentence.split(',')
            
        return sentences


    #This function splits sentences into words and stores them as a list.
    def word_split(self, text):
        sentences_list = []
        count = 0
        commas = []
        periods = []
        total_words = 0
        for sentence in text:
            count += 1
            words = sentence.split(' ')
            sentences_list.append(words)

            print('\nSentence ('+str(count)+') :\n'+ sentence)
            print('Words:'+'('+str(len(words))+')')

            total_words += len(words)

            for word in words:
            #Removing Commas from words
                # if word.contains(','):
                #     word.replace(',', '')
                # word = ''.join(char)            
                print('-> ' + word+' ('+str(len(word))+')')
            

            
        #This segment prints the Statistics of the tokenizer
        print('\nSummary:')
        print('Total Senctences: '+str(len(sentences_list)))
        print('Total number of Tokens: '+str(total_words)+'\n')
        return sentences_list
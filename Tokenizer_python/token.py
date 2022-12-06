#This function splits a paragraph into sentences and stores them as a list
# which it then returns a list of sentences.
class tokenizer: 
    def sentence_split(self, text):
        sentences = text.split('.')
        count = 0
        
        sentences.remove('') #This line removes the empty values from the list.
        print('\nTokenizer:\n'+text)
        print('sentences('+str(len(sentences))+') : ')
        for sentence in sentences:
            if (sentence != ''):
                print(' -> '+sentence)
                sentence.split(',')
            else:
                sentences.remove(sentence)
        return sentences


    #This function splits sentences into words and stores them as a list.
    def word_split(self, text):
        sentences_list = []
        count = 0
        total_words = 0
        for sentence in text:
            count += 1
            words = sentence.split(' ')

            print('\nSentence ('+str(count)+') :\n'+ sentence)
            print('Words:'+'('+str(len(words))+')')

            total_words += len(words);

            for word in words:
                #Removing Commas from words

                char = word.split()
                if (char.count(',')>=1):
                    char.remove(',')
                word = ''.join(char)            
                print('-> ' + word+' ('+str(len(word))+')')
            sentences_list.append(words)

            
        #This segment prints the Statistics of the tokenizer
        print('\nSummary:')
        print('Total Senctences: '+ str(len(sentences_list)))
        print('Total number of Tokens: '+str(total_words)+'\n')
        return sentences_list





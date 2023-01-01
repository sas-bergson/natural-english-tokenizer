#!/usr/bin/env python3
##
# @mainpage Tokenizer Project
#
# @section description_main Description
# The is the generated documentation for group 2's part of the project.
# generating source code documentation with Doxygen.
#
# @section notes_main Notes
# - The course project is highly experimental and will involve 3 students in this group
#
# Copyright (c) 2022 Compiler Construct.  All rights reserved.
##
# @file statement.py.py
#
# @brief Example Python program with Doxygen style comments.
#
# @section description_doxygen_example Description
# @section author_doxygen_example Author(s)
# - Created by Mboh Bless Pearl on 21/11/2022.
# - Modified by Fontem Favour on 21/11/2022.
# - Modified by Seukam Kamadeu Samira on 21/11/2022
# Copyright (c) 2022 Compiler construct.  All rights reserved.
# Imports

# import statement_tokenizer from class/statement.py
import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.append( "../")

from statement import statement_tokenizer
    
def main():
    """! @brief Example Python program with Doxygen style comments."""
    f = open('./assets/text.txt', 'r')
    # text = f.read()
    f.close()
    text = '.Disconsolate, the dragonflies dawdled along the dull ditch. Devouring the dewy delectables, they delighted in the damp darkness. Drawing nearer to the deep depths, they detected a distant droning. Dismayed, they diverted their course and descended downward. Discarding the dismal surroundings, they darted away.'
    tokenizer = statement_tokenizer()
    # print("The function of to get all the tokens is: ",
    #       tokenizer.getAllTokens(text))
    # print("THIS IS RESPONSIBLE FOR TOKEN RETENSION AND CHARACTER IDENTIFICATION",
    #       tokenizer.retainAllTokens(text))
    print("THIS IS RESPONSIBLE FOR IDENTIFICATION OF VALID SENTENCES AND ")
    sentences = tokenizer.peformSentenceSplit(text)
    print("the number of sentences is: ", len(sentences),"\n")
    for i in range(len(sentences)):
        sentence = sentences[i]
        print ("THE {} IS -> {}\n".format(i+1, sentence))
        type = tokenizer.sentence_type(sentence)
        print("the {} is a {}".format(i+1,type))
        print("="*50, "\n"*2)
    # print("THIS IS RESPONSIBLE FOR MATHING ALL WORDS STARTING AN A OR a")
    # print(tokenizer.matchAllWordsStartingWithA(text))
    # print("THIS IS A THAT PARTIAL MATCHES THE TEXT TYPES:")
    # words = tokenizer.performWordSplit(text)

    # for word in words:
    #     print(word+" "+tokenizer.fsa(word))

    print("THIS IS RESPONSIBLE FOR IDENTIFICATION OF VALID WORDS AND ")
    for i in range(len(sentences)):
        word = sentences[i]
        print(i+1 , " -------> ",  tokenizer.performWordSplit(word), "\n"*2)
    
    for i in range(len(sentences)):
        words = tokenizer.performWordSplit(sentences[i])
        print("="*20, "\n"*2)
        print("  the {} sentences have {} words".format(i + 1, len(words)))
        for word in words:
            print("the word is --> "+word+" | the word type --> "+tokenizer.wordType(word)+ " | the word length: "+str(len(word)) + "\n")

if __name__ == "__main__":
    main()

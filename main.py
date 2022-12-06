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

from statement import statement_tokenizer


def main():
    """! @brief Example Python program with Doxygen style comments."""
    f = open('./assets/text.txt', 'r')
    # text = f.read()
    f.close()
    text = 'This is a test designed to verify the behaviour\
        of the tokenizer. If it succeeds, we will move to the design of a file scanner.'
    tokenizer = statement_tokenizer()
    # print("The function of to get all the tokens is: ",
    #       tokenizer.getAllTokens(text))
    # print("THIS IS RESPONSIBLE FOR TOKEN RETENSION AND CHARACTER IDENTIFICATION",
    #       tokenizer.retainAllTokens(text))
    print("THIS IS RESPONSIBLE FOR IDENTIFICATION OF VALID SENTENCES AND ")
    sentences = tokenizer.peformSentenceSplit(text)
    print(sentences)
    # print("THIS IS RESPONSIBLE FOR MATHING ALL WORDS STARTING AN A OR a")
    # print(tokenizer.matchAllWordsStartingWithA(text))
    # print("THIS IS A THAT PARTIAL MATCHES THE TEXT TYPES:")
    # words = tokenizer.performWordSplit(text)

    # for word in words:
    #     print(word+" "+tokenizer.fsa(word))
    for word in sentences:
        print(tokenizer.performWordSplit(word))


if __name__ == "__main__":
    main()

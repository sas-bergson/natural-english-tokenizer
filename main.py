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
# - Created by Kila Frederick Kisife on 12/1/2022.
# - Modified by Dikuba Kindjel Alicia Ashley on 12/1/2022.
# Copyright (c) 2022 Compiler construct.  All rights reserved.
# Imports

from statement import statement_tokenizer


def main():
    """! @brief Example Python program with Doxygen style comments."""


    text = "Here comes the men in black. We are working together."

    tokenizer = statement_tokenizer()
    print("The function of to get all the tokens is: ",
          tokenizer.getAllTokens(text))
    print("This is the method is responsible for the token retension:",
          tokenizer.retainAllTokens(text))
    print("THIS IS RESPONSIBLE FOR IDENTIFICATION OF VALID SENTENCES AND ")
    print(tokenizer.peformSentenceSplit(text))
    print("THIS IS RESPONSIBLE FOR MATHING ALL WORDS STARTING AN A OR a")
    print(tokenizer.matchAllWordsStartingWithA(text))
    print("THIS IS A THAT PARTIAL MATCHES THE TEXT TYPES:")
    words = tokenizer.performWordSplit(text)

    # for word in words:
    #     print(word+tokenizer.fsa(word))


if __name__ == "__main__":
    main()
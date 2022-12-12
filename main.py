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
    text = f.read()
    f.close()
    tokenizer = statement_tokenizer()
    # print("THIS IS RESPONSIBLE FOR IDENTIFICATION OF VALID SENTENCES AND ")
    sentences = tokenizer.peformSentenceSplit(text)
    for sentence in sentences:
        # print(sentence+" Character Count: "+str(len(sentence)))
        tokenizer.identifyPartsOfSpeech(sentence)
    print("\n\n")
    print("part of speech classification")
    print("Nouns:", tokenizer.nounList)
    print("Verbs:", tokenizer.verbList)
    print("Adverbs:", tokenizer.adverbList)
    print("Adjectives:"+str(tokenizer.adjectiveList))
    print("pronoun:"+str(tokenizer.pronounList))
    print("Interjections:"+str(tokenizer.interjectionsList))
    print("Conjunctions:"+str(tokenizer.conjunctionsList))
    print("Unknown parts of speech:"+str(tokenizer.unknownList))


if __name__ == "__main__":
    main()

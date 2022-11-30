""" @brief Example Python program with Doxygen style comments."""
##
# @mainpage Natural english tokenizer
#
# @section description_main Description
# An Python program demonstrating how to tokenize a statement.
#
# @section notes_main Notes
#
# Copyright (c) 2022 Jean Edouard TCHECK.  All rights reserved.

import statement as st


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st = st.StatementTokenizer()
    st.tokenizer('This is a test designed to verify the behaviour\
        of the tokenizer. If it succeeds, we will move to the design of a file scanner.')


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
    # st.tokenizer('Students are not interested in building compilers. I will force them.')
    st.tokenizer('Nadir is too null. I will neutralize his distractions.')

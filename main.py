""" @brief Example Python program with Doxygen style comments."""
##
# @mainpage Natural english tokenizer
#
# @section description_main Description
# An Python program demonstrating how to tokenize a statement.
#
# @section notes_main Notes

import statement as st


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    statements = [
        'This is a test designed to verify the behaviour\
                of the tokenizer. If it succeeds, we will move to the design of a file scanner.',
        'Nadir is too null. He is too negligent.'
    ]
    st = st.StatementTokenizer()
    st.get_tokens(statements[1])
    print(st.__str__())


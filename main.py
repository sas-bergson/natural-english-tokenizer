""" @brief Example Python program with Doxygen style comments."""
##
# @mainpage Natural english tokenizer
#
# @section description_main Description
# An Python program demonstrating how to tokenize a statement.
#
# @section notes_main Notes

import compiler as cmp


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    statements = [
        'This is a test designed to verify the behaviour\
                of the tokenizer. If it succeeds, we will move to the design of a file scanner.',
        'Nadir is negligent and too null.'
    ]
    # 'Nadir is too null. He is too negligent.'
    cmp_object = cmp.Compiler(statements[1])
    # print(cmp_object.get_tokens())
    print(cmp_object.get_ast())


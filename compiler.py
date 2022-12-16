import tokenizer as tk
import parser as pr


class Compiler:

    def __init__(self, input_expression: str):
        self._statement = input_expression
        # given an input expression, create a set of tokens
        tk_object = tk.Tokenizer(input_expression)
        self._tokens = tk_object.get_tokens()
        # create an abstract syntax tree given those tokens
        pr_object = pr.Parser(self._tokens)
        self._ast = pr_object.parser()
        print(self._ast)
        # create a transformed AST given the existing one
        # newAst = transformer(ast)
        # stringify the transformed AST into an output expression
        # output = codeGenerator(newAst)

    def get_tokens(self):
        return self._tokens

    def get_ast(self):
        return self._ast


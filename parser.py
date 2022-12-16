import re
import conjunction as cjt


class Parser:

    def __init__(self, tokens):
        self._tokens = tokens
        self.conjunction = cjt.Conjunction()

    # The parse function creates an Abstract Syntax Tree given the computed
    # tokens from the previous function
    def parser(self):
        # keep track of position while iterating
        global current
        current = 0

        # nested walk function for building an abstract syntax tree
        def walk():
            # keep track of position while iterating?
            global current

            token = self._tokens[current]

            # If uppercase letter encountered, return a "CallSentence" node
            if re.match(re.compile(r"[A-Z]"), token.get('value')[0]):
                # store the name of operation
                node = {
                    'type': 'CallSentence',
                    'name': token.get('value'),
                    'params': []
                }
                # and this node will have child nodes as parameters
                # and input expression can have many nested expressions
                # so we'll use recursion to build a tree of relations!
                current += 1
                token = self._tokens[current]
                # until the expression ends with a full stop or interrogation point or exclamation point
                while current < len(self._tokens) and token.get('type') != '.' and token.get('type') != '?' \
                        and token.get('type') != '!':
                    # recursively add nodes to the params array via the walk function
                    node['params'].append(walk())
                    if current < len(self._tokens):
                        token = self._tokens[current]

                current += 1
                return node

            word = self.conjunction.find_word(token.get('value').lower())
            if word:
                print(word)
                current += 1
                return {
                    'type': word['type'],
                    'value': token.get('value')
                }
            else:
                current += 1
                return {
                    'type': token.get('type'),
                    'value': token.get('value')
                }

            # error if unknown type encountered
            raise TypeError(token.get('type'))

        # Let's initialize an empty Abstract Syntax Tree
        ast = {
            'type': 'Program',
            'body': []
        }
        # then populate it by calling the walk function
        # until the global current variable reaches the end of the token array
        while current < len(self._tokens):
            ast['body'].append(walk())

        # return the completed AST
        return ast

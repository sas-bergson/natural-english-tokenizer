import re

class Statement:

    def __init__(self, text:str)-> None:
        self.text = text
        self._statements = list(filter(lambda stmt: len(stmt)>0,
                                       self._parse_regex('[\w*\.{3}\s]*[^\.|\?|,|;]*[\.|\?|,|;]?')))
        self._tokens = self._parse_regex("[\w+\-*]+|\s+|[^\s\w]+")


    def _parse_regex(self, regex):
        regex = re.compile(regex)
        return regex.findall(self.text)

    def get_statements(self)->str:
        return "\n".join(
                [
                    f"statement {n} -> {statement} (length = {len(statement)})" \
                    for n, statement in enumerate(self._statements, 1)
                ]
            )

    def get_tokens(self)->str:
        return "\n".join(
                    [
                        f"token {n} -> {token} (length = {len(token)})" 
                        for n, token in enumerate(self._tokens, 1)
                    ]
            )

if __name__ == "__main__":
    stmt = Statement('This... is a rendez-vous (test) designed to verify the behaviour\
        of the tokenizer. If it succeeds, we will move to the design of a file scanner.')
    print(stmt.get_statements())
    print()
    print(stmt.get_tokens())        
        
    

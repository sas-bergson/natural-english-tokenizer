import json
from Tokenizer import Tokenizer
class Search():
    def __init__(self)->None:
        self._myjsonfile = open('Tokenizer\dictionary.json','r')
        self._jsondata = self._myjsonfile.read()

        self._obj=json.loads(self._jsondata)

        self._nouns=self._obj['nouns']
        self._verbs=self._obj['verbs']
        self._pronouns=self._obj['pronouns']
        self._conjunctions=self._obj['conjunctions']
        self._articles=self._obj['articles']
        self._determiners=self._obj['determiners']
    
    def search(self)->list:
        t=Tokenizer()
        self._tokens=t.tokenizer()
        for i in self._nouns:
            for j in self._tokens:
                if j==i:
                    print(j,"is a noun","appears",self._tokens.count(j),"times")
        for i in self._verbs:
            for j in self._tokens:
                if j==i:
                    print(j,"is a verb","appears",self._tokens.count(j),"times")
        for i in self._pronouns:
            for j in self._tokens:
                if j==i:
                    print(j,"is a pronoun","appears",self._tokens.count(j),"times")
        for i in self._articles:
            for j in self._tokens:
                if j==i:
                    print(j,"is an article","appears",self._tokens.count(j),"times")
        for i in self._conjunctions:
            for j in self._tokens:
                if j==i:
                    print(j,"is a conjunction","appears",self._tokens.count(j),"times")
        for i in self._determiners:
            for j in self._tokens:
                if j==i:
                    print(j,"is a determiner","appears",self._tokens.count(j),"times")
        return [self._determiners,self._articles,self._conjunctions,self._nouns,self._verbs,self._pronouns]
        
        


s=Search()
s.search()

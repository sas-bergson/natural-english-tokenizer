import re
from PyDictionary import PyDictionary
#pattern is 
#2 lower case letters
#between 1 to 3 digits
#2 upper case letters 
#one symbol



# class Regex():
#     def __init__(self):
        # self.pattern = re.compile("^[a-z]{2}[0-9]{1,3}[A-Z]{2}[^a-zA-Z0-9]{1}$")
#         print(self.pattern.search("rt45UI. rt45UI."))
#         print(self.pattern.search("r45DavE"))
# r=Regex()

class Regex():

    """
    A class used to represent the steps i used in tokenizing sentences and repressenting tokens as parts of speech

    ...

    Attributes
    ----------

    Methods
    -------
    tokenize()
        splits the matching sentence that passed the regex text
    
    classification()
        gets the tokens from the splited sentence and passed it through some criteria to determine the parts of speech of each token
    """


    def __init__(self)->None:

        """
        This method compares a sentence to a desired regex pattern


        Attributes
        ----------

        Excepts
        -------
        prints no matching sentence if the comparing sentence doesn't match the desired pattern

        Returns
        -------
        returns None
        """
        
        try:
            self._sentence_pattern = re.compile("^[A-Z\s]+[a-z\s]+\.$")
            self._matching_string=self._sentence_pattern.search("Come get your pencil.")[0]
            print("matching sentence is \t" + self._matching_string)
            # self.tokenize()
            # self.classification()
        except:
            print("\t no matching sentence found")

    def tokenize(self)->list:
        """
        This method gets the matching sentence and splits it into tokens 


        Attributes
        ----------

        Excepts
        -------

        Returns
        -------
        returns a list of tokens
        """
        self._tokens = self._matching_string.split()
        print(self._tokens)
        return self._tokens
        
    
    def classification(self)->str:
        """
        This method gets the tokens and classify them through parts of speech


        Attributes
        ----------
        dictionary: a pydictionary object

        Excepts
        -------
        prints no matching part of speech if the comparing tokens doesn't match the desired pattern

        Returns
        -------
        returns a String
        """
        dictionary = PyDictionary() 
        for i in self._tokens:
            print(f'token \t{i}', '\t',dictionary.meaning(i))
        # self._noun_pattern=re.compile("^[A-Z|a-z]+[^0-9]+[^A-Za-z0-9]+$")
        # for i in self._tokens:
        #     try:
        #         self._noun_pattern.search(i)[0]
        #         n=self._noun_pattern.search(i)[0]
        #         print("noun found\t"+n)
        #     except:
        #         print("no match for noun")
        # self._noun_pattern = re.compile("^[]$")


    def search_partsOfSpeech(self):
        with open('dictionary.txt','r') as file:
            content = file.read()
            for i in self._tokens:
                if i in content:
                    print(i +'\t found')
                else:
                    print("not found")
            # if self._tokens in content

r=Regex()
r.tokenize()
r.search_partsOfSpeech()
# r.search_partsOfSpeech('C:\Users\Dave237\Tokenizer\dictionary.txt',self._tokens)
# r.classification()

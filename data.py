import json
import os

class Dict_Data:
    """Fetches Data from a json dictionary and parses it for tokonization purpose"""

    def __init__(self, alphabet_letter="Q", dir="data") -> None:
        self.__data = {
            "noun":set(), 
            "pronoun":set(), 
            "verb":set(),
            "article":set(),
            "adjective":set(),
            "adverb":set(),
            "preposition":set(),
            "conjunction":set(),
            "interjection":set()
        }
        self.__letter= "".join(["D", alphabet_letter])
        self.__dir = dir
        self.__load_data()

    def __load_data(self) -> None:
        """Never all this method it is conviniently called at the proper moment at run time"""

        path = os.path.join(self.__dir, self.__letter)
        path += ".json"
        try:
            with open(path) as file:
                data = json.load(file)
            for word, explanations in data.items():
                meanings = explanations.get("MEANINGS", {})
                for definition in meanings.values():
                    if definition:
                        fund_type = definition[0].lower()
                        if fund_type in self.__data:
                            self.__data[fund_type].add(word)
        except FileNotFoundError as e:
            print(e)
    
    @property
    def data(self):
        """converts all the sets in the __data private property for it to be conveniently be stored in json"""

        return {key:list(value) for key, value in self.__data.items()}
        

if __name__ == "__main__":
    import string
    A_Z = list(string.ascii_uppercase)
    os.makedirs("data_treamed", exist_ok=True)
    for letter in A_Z:
        d_d = Dict_Data(alphabet_letter=letter)
        with open("data_treamed/Bayi_"+letter+".json", "w") as file:
            json.dump(d_d.data, file, indent=4)
    


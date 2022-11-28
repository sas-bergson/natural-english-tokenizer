
import json
from difflib import get_close_matches

from nltk.corpus import stopwords

data = json.load(open('letter_q_dictionary.json'))

word = input('enter a word: ').lower()
possible = get_close_matches(word, data.keys())

def translate(x):
    if x in data:
        return data[x]
    elif len(possible) > 0:
        newword = input(f"Did you mean to say: {possible}:").lower()
        return data[newword]
    else:
        return "could'nt find word"

print(translate(word))


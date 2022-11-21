import os
import re


class statement_tokenizer:

    def __init__(self):
        self._pattern = 'r"[A-Z]+[a-z]*\s\."'
        self._regex = re.compile(self._pattern)
        self._tokens = []

    def get_tokens(self, text) -> list:
        self._tokens = self._regex.split(text)
        return self._tokens

    def __str__(self) -> str:
        for s in self._tokens:
            print(f"statement -> {s}")

# splitting into phrases
    def sentence_parser(self, text : str):
        temp_word = ""
        word = ""
        phrase = []
        list_of_phrases = []
        for char in text:
            temp_word += char
            if char == " ":
                word = temp_word.rstrip()
                phrase.append(word)
                temp_word = ""
                word = ""
            if char == ".":
                list_of_phrases.append(phrase)
                temp_word = ""
                phrase = []

        return list_of_phrases

# splitting into words
    def word_parser(self, phrase: str):
        temp_word = ""
        word = ""
        tokens = []
        for char in phrase:
            temp_word += char
            if char == " ":
                word = temp_word.strip()
                tokens.append(word)
                temp_word = ""
                word = ""

        return tokens







text = "It was their first date and she had been looking forward to it the entire week. She had her eyes on him for months, and it had taken a convoluted scheme with several friends to make it happen, but he'd finally taken the hint and asked her out. After all the time and effort she'd invested into it, she never thought that it would be anything but wonderful. It goes without saying that things didn't work out quite as she expected. Matt told her to reach for the stars, but Veronica thought it was the most ridiculous advice she'd ever received. Sure, it had been well-meaning when he said it, but she didn't understand why anyone would want to suggest something that would literally kill you if you actually managed to achieve it. Dragons don't exist they said. They are the stuff of legend and people's imagination. Greg would have agreed with this assessment without a second thought 24 hours ago. But now that there was a dragon staring directly into his eyes, he questioned everything that he had been told."



obj = statement_tokenizer().sentence_parser(text)
obj1 = statement_tokenizer().word_parser(text)
# print(obj)
ren=0
# doesnt print the last word of every sentence
for phrase in obj:
    print(f"phrase {ren}: {phrase}")
    ren += 1

for word in obj1:
    print(f"word {ren}: {word}")
    ren += 1


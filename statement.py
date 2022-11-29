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
    def sentence_scanner(self, text : str):
        temp_phrase = ""
        list_of_phrases = []
        no_of_sentences = 0
        for char in text:
            temp_phrase += char
            if char == ".":
                no_of_sentences += 1
                list_of_phrases.append(temp_phrase.strip())
                temp_phrase = ""
        print("no of sentences: ", no_of_sentences)
        return list_of_phrases

# output from sentence_parser in more presentable way
    def sentence_presentation(self, array_of_phrases: []):
        phrase_count = 0
        for phrase in array_of_phrases:
            print(f"phrase {phrase_count + 1}: {phrase}")
            phrase_count += 1

# splitting into words
    def word_scanner(self, array_of_phrases: []):
        word_count = 0
        for phrase in array_of_phrases:
            temp_words = phrase.split()
            for word in temp_words:
                self._tokens.append(word.lower())
                temp_words = []
        print("word count: ", self._tokens.__len__())
        return self._tokens







text = "It was their first date and she had been looking forward to it the entire week. She had her eyes on him for months, and it had taken a " \
       "convoluted scheme with several friends to make it happen, but he'd finally taken the hint and asked her out. After all the time and effort " \
       "she'd invested into it, she never thought that it would be anything but wonderful. It goes without saying that things didn't work out quite " \
       "as she expected. Matt told her to reach for the stars, but Veronica thought it was the most ridiculous advice she'd ever received. Sure, it " \
       "had been well-meaning when he said it, but she didn't understand why anyone would want to suggest something that would literally kill you " \
       "if you actually managed to achieve it. Dragons don't exist they said. They are the stuff of legend and people's imagination. Greg would " \
       "have agreed with this assessment without a second thought 24 hours ago. But now that there was a dragon staring directly into his eyes, " \
       "he questioned everything that he had been told."

text1 = "This is a test designed to verify the behaviour of the tokenizer. If it succeeds, we will move to the design of a file scanner."
# printing array of phrases
obj = statement_tokenizer().sentence_scanner(text1)
#print(obj)

# more comprehensive presentation of array of phrases
sentence_presentation = statement_tokenizer().sentence_presentation(obj)

# printing tokens
tokens = statement_tokenizer().word_scanner(obj)
print(tokens)



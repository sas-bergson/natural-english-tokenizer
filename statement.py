import os
import re


class statement_tokenizer:

    def __init__(self):
        self._pattern = 'r"[A-Z]+[a-z]*\s\."'
        self._regex = re.compile(self._pattern)
        self._stop_mark = ".?!"
        self._tokens = []
        self._stopwords = ""
        self.api_url = f""

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
            if char in self._stop_mark:
                no_of_sentences += 1
                list_of_phrases.append(temp_phrase.strip())
                temp_phrase = ""
        print("no of sentences: ", no_of_sentences)

        return list_of_phrases

# output from sentence_parser in more presentable way
    def sentence_presentation(self, array_of_phrases: []):
        phrase_count = 0
        for phrase in array_of_phrases:
            print(f"phrase_{phrase_count + 1}: {phrase}")
            phrase_count += 1









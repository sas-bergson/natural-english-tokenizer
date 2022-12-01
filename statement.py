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

# removes stop words, negated words and conjectures from tokens
    def tokens_cleanup(self, tokens: []):
        clean_tokens = []

        for word in tokens:
            temp_char_pos = 0
            temp_char = word[temp_char_pos]
            prev_char_pos = temp_char_pos - 1
            prev_char = word[prev_char_pos]
            next_char_pos = temp_char_pos + 1
            next_char = word[next_char_pos]
            word_size = len(word)

            while temp_char_pos < word_size:
                if prev_char_pos == -1:
                    prev_char = ""
                if next_char_pos == word_size:
                    next_char = ""

        # # checking for negated words
        #         if temp_char == "'" and (prev_char == "n" and next_char == "t"):
        #             temp_word = word[:3]
        #             clean_tokens.append(temp_word.strip())
        #             temp_word = ""
        #
        # # checking for stopwords
        #         if word in self._stopwords:
        #             temp_word = "stopword"
        #             clean_tokens.append(temp_word)
        #             clean_tokens.pop()
        #
                temp_char_pos += 1
                clean_tokens.append(word)

            return clean_tokens




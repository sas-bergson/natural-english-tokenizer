import os
import re


class statement_tokenizer:
    def __init__(self):
        self._pattern = 'r"[A-Z]+[a-z]*\s\."'
        self._regex = re.compile(self._pattern)
        self._stop_mark = ".?!"
        self._tokens = []
        self._stopwords = ""
        self._endpoint = {
                          "Entries": "Entries",
                          "Lemmas": "Lemmas",
                          "Search": "Search",
                          "Translations": "Translations",
                          "Thesaurus": "Thesaurus",
                          "Utility": "Utility",
                          "Sentences": "Sentences",
                          "Words": "Words",
                          "Inflections": "Inflections"
                         }
        self._lang_code = {
                            "English": "EN",
                            "Arabic": "AR",
                            "Chinese": "ZH",
                            "French": "FR",
                            "German": "DE",
                            "Hausa": "HA",
                            "Igbo": "IG",
                            "Portuguese": "PT",
                            "Russian": "RU",
                            "Spanish": "ES",
                            "Yoruba": "YO",
                          }
        self._word_id = "Hello"
# refer https://developer.oxforddictionaries.com/documentation/making-requests-to-the-api
# for more info on the endpoint, lang_code and word_id
        self.api_url = f"https://od-api.oxforddictionaries.com/api/v2/{self._endpoint}/{self._lang_code}/{self._word_id}"

    def get_tokens(self, text) -> list:
        self._tokens = self._regex.split(text)
        return self._tokens

    def __str__(self) -> str:
        for s in self._tokens:
            print(f"statement -> {s}")

# splitting into phrases
    def sentence_scanner(self, text: str):
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

# splitting into words and making lowercase
    def word_scanner(self, array_of_phrases: []):
        for phrase in array_of_phrases:
            temp_words = phrase.split()
            for word in temp_words:
                self._tokens.append(word.lower())

        print("word count: ", self._tokens.__len__())
        return self._tokens

# lemmatizing tokens
    def tokens_cleanup(self, tokens: []):
        clean_tokens = []
        for word in tokens:
            for char in word:
        # checking for ' in words
                if char == "'":
                    temp_char_pos = word.find(char)
                    next_char_pos = temp_char_pos + 1
                    next_char = word[next_char_pos]
                    prev_char_pos = temp_char_pos - 1
                    prev_char=word[prev_char_pos]
                # checking for negated short form words e.g. isn't
                    if prev_char == "n" and next_char == "t":
                        word = word[0: prev_char_pos]
                        clean_tokens.append(word)
                # checking for past or future short form words e.g. he's, they'd
                    if next_char == "d" or next_char == "s":
                        word = word[0: temp_char_pos]
                        clean_tokens.append(word)

                    word = ""
            clean_tokens.append(word)

    # cleaning up new tokens list
        for word in clean_tokens:
            if word == "":
                word_pos = clean_tokens.index(word)
                clean_tokens.pop(word_pos)

        print("refined word count: ", len(clean_tokens))
        return clean_tokens

# returns api with desired arguments
    def api_organiser(self, endpoint, lang_code, word_id):
        self.api_url = f"https://od-api.oxforddictionaries.com/api/v2/{endpoint}/{lang_code}/{word_id}"
        print(self.api_url)
        return self.api_url




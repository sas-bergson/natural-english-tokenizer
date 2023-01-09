import os
import re


class statement_tokenizer:
    def __init__(self):
        self._pattern = 'r"[A-Z]+[a-z]*\s\."'
        self._regex = re.compile(self._pattern)
        self._stop_mark = ".?!"
        self._tokens = []
        self._stopwords = ""
    # parts of speech
        self._interjections = ["ah", "alas", "dear", "eh", "er", "god", "hello", "holla", "hi", "hey", "hmm", "oh", "o", "ok", "okay", "ouch", "uh", "huh", "um", "wow"]
        self._conjunctions = ["accordingly", "actually", "after", "afterwards", "also", "and", "another", "because", "before", "besides", "briefly", "but", "consequently",
                              "conversely", "finally", "furthermore", "gradually", "hence", "however", "least", "first", "second", "last", "later", "meanwhile", "moreover",
                              "nevertheless", "next", "nonetheless", "now", "nor", "or", "presently", "similarly", "since", "so", "soon", "still", "subsequently", "then",
                              "thereafter", "therefore", "third", "thus", "too", "ultimately", "what", "whatever", "whoever", "whereas", "whomever", "when", "while", "yet"
        ]
        self._adverbs = ["abnormally", "absentmindedly", "accidentally", "actually", "adventurously", "afterwards", "almost", "always", "annually", "anxiously", "arrogantly",
                         "awkwardly", "bashfully", "beautifully", "bitterly", "bleakly", "blindly", "blissfully", "boastfully", "boldly", "bravely", "briefly", "brightly",
                         "briskly", "broadly", "busily", "calmly", "carefully", "carelessly", "cautiously", "certainly", "cheerfully", "clearly", "cleverly", "closely",
                         "coaxingly", "colorfully", "commonly", "continually", "coolly", "correctly", "courageously", "crossly", "cruelly", "curiously", "daily", "daintily",
                         "dearly", "deceivingly", "deeply", "defiantly", "deliberately", "delightfully", "diligently", "dimly", "doubtfully", "dreamily", "easily",  "elegantly",
                         "energetically", "enormously", "enthusiastically", "equally", "especially", "evenly", "eventually", "exactly", "excitedly", "extremely", "fairly",
                         "faithfully", "famously", "far", "fast", "fatally", "ferociously", "fervently", "fiercely", "fondly", "foolishly", "fortunately", "frankly",
                         "frantically", "freely", "frenetically", "frightfully", "fully", "furiously", "generally", "generously", "gently", "gladly", "gleefully", "gracefully",
                         "gratefully", "greatly", "greedily", "happily", "hastily", "healthily", "heavily", "helpfully", "helplessly", "highly", "honestly", "hopelessly",
                         "hourly", "hungrily", "immediately", "innocently", "inquisitively", "instantly", "intensely", "intently", "interestingly", "inwardly", "irritably",
                         "jaggedly", "jealously", "jovially", "joyfully", "joyously", "jubilantly", "judgmentally", "justly", "keenly", "kiddingly", "kindheartedly", "kindly",
                         "knavishly", "knowingly", "knowledgeably", "kookily", "lazily", "lightly", "likely", "limply", "lively", "loftily", "longingly", "loosely", "loudly",
                         "lovingly", "loyally", "madly", "majestically", "meaningfully", "mechanically", "merrily", "miserably", "mockingly", "monthly", "more", "mortally",
                         "mostly", "mysteriously", "naturally", "hopelessly", "hourly", "hungrily", "immediately", "innocently", "inquisitively", "instantly", "intensely",
                         "intently", "interestingly", "inwardly", "irritably", "jaggedly", "jealously", "jovially", "joyfully", "joyously", "jubilantly", "judgmentally",
                         "justly", "keenly", "kiddingly", "kindheartedly", "kindly", "knavishly", "knowingly", "knowledgeably", "kookily", "lazily", "less", "lightly", "likely",
                         "limply", "lively", "loftily", "longingly", "loosely", "loudly", "lovingly", "loyally", "madly", "majestically", "meaningfully", "mechanically",
                         "merrily", "miserably", "mockingly", "monthly", "more", "mortally", "mostly", "mysteriously", "naturally", "nearly", "neatly", "nervously", "never",
                         "nicely", "noisily", "not", "obediently", "obnoxiously", "oddly", "offensively", "officially", "often", "only", "openly", "optimistically",
                         "overconfidently", "painfully", "partially", "patiently", "perfectly", "physically", "playfully", "politely", "poorly", "positively", "potentially",
                         "powerfully", "promptly", "properly", "punctually", "quaintly", "queasily", "queerly", "questionably", "quicker", "quickly", "quietly", "quirkily",
                         "quizzically", "randomly", "rapidly", "rarely", "readily", "really", "reassuringly", "recklessly", "regularly", "reluctantly", "repeatedly",
                         "reproachfully", "restfully", "righteously", "rightfully", "rigidly", "roughly", "rudely", "safely", "scarcely", "scarily", "searchingly", "sedately",
                         "seemingly", "seldom", "selfishly", "separately", "seriously", "shakily", "sharply", "sheepishly", "shrilly", "shyly", "silently", "sleepily", "slowly",
                         "smoothly", "softly", "solemnly", "solidly", "sometimes", "soon", "speedily", "stealthily", "sternly", "strictly", "successfully", "suddenly",
                         "supposedly", "surprisingly", "suspiciously", "sweetly", "swiftly", "sympathetically", "tenderly", "tensely", "terribly", "thankfully", "thoroughly",
                         "thoughtfully", "tightly", "tomorrow", "too", "tremendously", "triumphantly", "truly", "truthfully", "rightfully", "scarcely", "searchingly",
                         "sedately", "seemingly", "selfishly", "separately", "seriously", "sheepishly", "smoothly", "solemnly", "sometimes", "speedily", "stealthily",
                         "successfully", "suddenly", "supposedly", "surprisingly", "suspiciously", "sympathetically", "tenderly", "thankfully", "thoroughly", "thoughtfully",
                         "tomorrow", "tremendously", "triumphantly", "truthfully", "ultimately", "unabashedly", "unaccountably", "unbearably", "unethically", "unexpectedly",
                         "unfortunately", "unimpressively", "unnaturally", "unnecessarily", "upbeat", "upright", "upward", "urgently", "usefully","uselessly", "usually",
                         "utterly", "vacantly", "vaguely", "vainly", "valiantly", "vastly", "verbally", "very", "viciously", "victoriously", "violently", "vivaciously",
                         "voluntarily", "warmly", "weakly", "wearily", "well", "wetly", "wholly", "wildly", "willfully", "wisely", "woefully", "wonderfully", "worriedly",
                         "wrongly", "yawningly", "yearly", "yearningly", "yesterday", "yieldingly", "youthfully", "zealously", "zestfully", "zestily"
        ]
        self._prepositions = ["about", "after", "ago", "around", "at", "before", "by", "circa", "during", "following", "for", "from", "gone", "in", "on", "past", "since",
                              "until", "till", "aboard", "above", "across", "against", "alongside", "amid", "among", "apart", "from", "astride", "at", "atop", "behind", "below",
                              "beneath", "beside", "between", "beyond", "by", "close", "to", "far", "from", "in", "inside", "into", "minus", "near", "of", "off", "on",
                              "onto", "Upon", "opposite", "out", "outside", "over", "round", "through", "throughout", "to", "together", "with", "toward", "under", "underneath",
                              "with", "within", "without", "above", "across", "against", "ahead", "along", "amid", "around", "away", "behind", "below", "beneath", "down", "into",
                              "off", "on", "onto", "over", "past", "round", "through", "under", "up", "via", "about", "anti", "as", "beside", "by", "but", "concerning",
                              "considering", "counting", "despite", "except", "given", "including", "less", "like", "notwithstanding", "of", "pending", "per", "plus", "pro",
                              "than", "unlike", "versus", "with", "worth"
        ]
        self._pronouns = ["all", "another", "any", "anybody", "anyone", "anything", "as", "aught", "both", "each", "other", "either", "enough", "everybody", "everyone",
                          "everything", "few", "he", "her", "hers", "herself", "him", "himself", "his", "I", "idem", "it", "its", "itself", "many", "me", "mine", "most", "my",
                          "myself", "naught", "neither", "no", "one", "nobody", "none", "nothing", "nought", "another", "other", "our", "ours", "ourself", "ourselves",
                          "several", "she", "some", "somebody", "someone", "something", "somewhat", "such", "suchlike", "that", "thee", "their", "theirs", "theirself",
                          "theirselves", "them", "themself", "themselves", "there", "these", "they", "thine", "this", "those", "thou", "thy", "thyself", "us", "we", "what",
                          "whatever", "whatnot", "whatsoever", "whence", "where", "whereby", "wherefrom", "wherein", "whereinto", "whereof", "whereon", "wherever",
                          "wheresoever", "whereto", "whereunto", "wherewith", "wherewithal", "whether", "which", "whichever", "whichsoever", "who", "whoever", "whom",
                          "whomever", "whomso", "whomsoever", "whose", "whosever", "whosesoever", "whoso", "whosoever", "ye", "yon", "yonder", "you", "your", "yours",
                          "yourself", "yourselves"
        ]
        self._adjectives = ["adorable", "adventurous", "aggressive", "agreeable", "alert", "alive", "amused", "angry", "annoyed", "annoying", "anxious", "arrogant", "ashamed",
                            "attractive", "average", "awful", "bad", "beautiful", "better", "bewildered", "black", "bloody", "blue", "blushing", "bored", "brainy", "brave",
                            "breakable", "bright", "busy", "calm", "careful", "cautious", "charming", "cheerful", "clean", "clear", "clever", "cloudy", "clumsy", "colorful",
                            "combative", "comfortable", "concerned", "condemned", "confused", "cooperative", "courageous", "crazy", "creepy", "crowded", "cruel", "curious",
                            "cute", "dangerous", "dark", "dead", "defeated", "defiant", "delightful", "depressed", "determined", "different", "difficult", "disgusted",
                            "distinct", "disturbed", "dizzy", "doubtful", "drab", "dull", "eager", "easy", "elated", "elegant", "embarrassed", "enchanting", "encouraging",
                            "energetic", "enthusiastic", "envious", "evil", "excited", "expensive", "exuberant", "fair", "faithful", "famous", "fancy", "fantastic", "fierce",
                            "filth", "fine", "foolish", "fragile", "frail", "frantic", "friendly", "frightened", "funny", "gentle", "gifted", "glamorous", "gleaming", "glorious",
                            "good", "gorgeous", "graceful", "grieving", "grotesque", "grumpy", "handsome", "happy", "healthy", "helpful", "helpless", "hilarious", "homeless",
                            "homely", "horrible", "hungry", "hurt", "ill", "important", "impossible", "inexpensive", "innocent", "inquisitive", "itchy", "jealous", "jittery",
                            "jolly", "joyous", "kind", "lazy", "light", "lively", "lonely", "long", "lovely", "lucky", "magnificent", "misty", "modern", "motionless", "muddy",
                            "mushy", "mysterious", "nasty", "naughty", "nervous", "nice", "nutty", "obedient", "obnoxious", "odd", "open", "outrageous", "outstanding", "panicky",
                            "perfect", "plain", "pleasant","poised", "poor", "powerful", "precious", "prickly", "proud", "putrid", "puzzled", "quaint", "real", "relieved",
                            "repulsive", "rich", "scary", "selfish", "shiny", "shy", "silly", "sleepy", "smiling", "smoggy", "sore", "sparkling", "splendid", "spotless",
                            "stormy", "strange", "stupid", "successful", "super", "talented", "tame", "tasty", "tender", "tense", "terrible", "thankful", "thoughtful",
                            "thoughtless", "tired", "tough", "troubled", "ugliest", "ugly", "uninterested", "unsightly", "unusual", "upset", "uptight", "vast", "victorious",
                            "vivacious", "wandering", "weary", "wicked", "wide", "wild", "witty", "worried", "worrisome", "wrong", "zany", "zealous"
        ]
        self._articlesOfSpeech = ["the", "a", "an"]
        self._verbs = ["was", "has", "had", "been", "said"]
        self.nouns = []
    # api variables
        self._endpoint = {
                          "entries": "Entries",
                          "lemmas": "Lemmas",
                          "search": "Search",
                          "translations": "Translations",
                          "thesaurus": "Thesaurus",
                          "utility": "Utility",
                          "sentences": "Sentences",
                          "words": "Words",
                          "inflections": "Inflections"
                         }
        self._lang_code = {
                            "english": "EN",
                            "arabic": "AR",
                            "chinese": "ZH",
                            "french": "FR",
                            "german": "DE",
                            "hausa": "HA",
                            "igbo": "IG",
                            "portuguese": "PT",
                            "russian": "RU",
                            "spanish": "ES",
                            "yoruba": "YO",
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

# parsing clean-up tokens into their meanings
    def token_parser(self, clean_tokens: []):
        parsed_data = {}
        for token in clean_tokens:
            if token in self._articlesOfSpeech:
                parsed_data[token] = "article of speech"
            elif token in self._interjections:
                parsed_data[token] = "interjection"
            elif token in self._conjunctions:
                parsed_data[token] = "conjunction"
            elif token in self._adverbs:
                parsed_data[token] = "adverb"
            elif token in self._prepositions:
                parsed_data[token] = "preposition"
            elif token in self._pronouns:
                parsed_data[token] = "pronoun"
            elif token in self._adjectives:
                parsed_data[token] = "adjective"
        # checking verbs
            elif token.endswith("ing") or token.endswith("ed") or token in self._verbs:
                parsed_data[token] = "verb"
        # checking nouns
            # converting values of dict into list and targetting last value
            elif list(parsed_data.values())[-1] or " " == "conjunction":
                parsed_data[token] = "noun"
            else:
                parsed_data[token] = "N/A"

        for key, value in parsed_data.items():
            print(key, ":", value)

# returns api with desired arguments
    def api_organiser(self, endpoint, lang_code, word_id):
        self.api_url = f"https://od-api.oxforddictionaries.com/api/v2/{endpoint}/{lang_code}/{word_id}"
        print(self.api_url)
        return self.api_url
# what you have to do now is make the api work and check the meanings

import regex as re
class DemoTokenizer:    
# ! function to enable character recognition
    def fmtcharRecog(text):
        new_text = ""
        for i in range(len(text)):
            if re.match(r'\.|,|\'|\)|\}|\]|\:|\;', text[i]):
                new_text = new_text+" "+text[i]
            elif re.match(r'\(|\{|\[|\s', text[i]):
                new_text = new_text+text[i]+" "
            else:
                new_text = new_text+text[i]
        return new_text

# ! sentences splitting
    def performSentenceSplit(text):
        formated_text = ""
        for i in range(len(text)):
            if re.match(r'\.', text[i]):
                formated_text = formated_text+text[i]+" .sfmat"
            else:
                formated_text = formated_text+text[i]
        return formated_text.split(" .sfmat")
    @classmethod
    def performWordSplit(self,text):
        data = self.fmtcharRecog(text).strip()
        return data.split(" ")
#! tagging String
  
    def tag(lstData):
        # generate a list of colors
        colors = ["green", "blue", "orange", "violet", "red"]
        tagged = []
        for word in lstData:
            if word == "sunday" or word == "monday" or word == "tuseday" or word == "wednesday" or word == "thursday" or word == "friday" or word == "saturday" or re.search(r'.*ance$', word) or re.search(r'.*ers$', word) or re.search(r'.*ence$', word) or re.search(r'.*ar$', word) or re.search(r'.*er$', word) or re.search(r'.*ir$', word) or re.search(r'.*or$', word) or re.search(r'.*ur$', word) or re.search(r'.*ism$', word) or re.search(r'.*ment$', word) or re.search(r'.*age$', word) or re.search(r'.*hood$', word) or re.search(r'.*ness$', word) or re.search(r'.*irt$', word) or re.search(r'.*er$', word) or re.search(r'.*bots', word) or re.search(r'.*ty$', word):
                tagged.append(word+", noun   ")
            elif re.search(r'.*able$', word) or re.search(r'.*ible$', word) or re.search(r'.*wn$', word) or re.search(r'.*wns$', word) or re.search(r'.*has$', word) or re.search(r'.*ant$', word) or re.search(r'.*ent$', word) or re.search(r'.*ists$', word) or re.search(r'.*ist$', word) or re.search(r'.*ous$', word) or re.search(r'.*ing$', word) or re.search(r'.*ful$', word) or re.search(r'.*ish', word) or re.search(r'.*ize$', word) or re.search(r'.*ate$', word) or re.search(r'.*ify$', word) or re.search(r'.*ise$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ize', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ize$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ize$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ize$', word) or re.search(r'.*ate$', word) or re.search(r'.*ise$', word) or re.search(r'.*ize$', word) or re.search(r'.*ed$', word) or re.search(r'.*ate$', word) or re.search(r'.*ons$', word) or re.search(r'.*ing', word) or re.search(r'.*de', word) or re.search(r'.*ound', word):
                tagged.append(word+", verb   ")
            elif re.search(r'.*ly$', word) or re.search(r'.*ry$', word) or word == "right" or word == "wrong" or re.search(r'.*here$', word) or word == 'soon' or re.search(r'.*soon$', word) or re.search(r'.*times$', word) or re.search(r'.*in$', word) or re.search(r'.*here$', word):
                tagged.append(word+", adverb   ")
            elif word == "":
                tagged = tagged
            elif re.search(r'.*zing$', word) or re.search(r'.*sive$', word) or re.search(r'.*ive$', word) or re.search(r'.*tic$', word) or re.search(r'.*tle$', word) or word in colors:
                tagged.append(word+", adjectives   ")
            else:
                tagged.append(word+", none")
        return tagged

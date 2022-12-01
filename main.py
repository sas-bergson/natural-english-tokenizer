from statement import statement_tokenizer

# lmdfvnmlfknmlfknlfknlmfknkflvn

if __name__ == "__main__":

    text = "It was their first date and she had been looking forward to it the entire week. She had her eyes on him for months, and it had taken " \
           "a convoluted scheme with several friends to make it happen, but he'd finally taken the hint and asked her out. After all the time and " \
           "effort she'd invested into it, she never thought that it would be anything but wonderful. It goes without saying that things didn't " \
           "work out quite as she expected. Matt told her to reach for the stars, but Veronica thought it was the most ridiculous advice she'd " \
           "ever received. Sure, it had been well-meaning when he said it, but she didn't understand why anyone would want to suggest something " \
           "that would literally kill you if you actually managed to achieve it. Dragons don't exist they said. They are the stuff of legend and " \
           "people's imagination. Greg would have agreed with this assessment without a second thought 24 hours ago. But now that there was a " \
           "dragon staring directly into his eyes, he questioned everything that he had been told."

    text1 = "This is a test designed to verify the behaviour of the tokenizer. If it succeeds, we will move to the design of a file scanner."

# printing array of phrases
    print("\n 1. Sentence count and poor presentation...")
    obj = statement_tokenizer()
    sentencized_text = obj.sentence_scanner(text)
    print(sentencized_text)

# more comprehensive presentation of array of phrases
    print("\n 2. Proper presentation...")
    sentence_presentation = obj.sentence_presentation(sentencized_text)

# printing tokens
    print("\n 3. Unclean tokens...")
    tokens = obj.word_scanner(sentencized_text)
    print(tokens)

# printing cleaned up tokens
#     print("\n 4. Cleaned up tokens...")
#     clean_tokens = obj.tokens_cleanup(tokens)
#     print(clean_tokens)

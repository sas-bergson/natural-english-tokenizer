# Natural language Tokenization 
#
# This is a simple example of how to use the Tokenizer class to tokenize a text.
 The goal of this at the end of the course is to have to understand the code and be able to use it in your own projects.
<!-- image describing tokenization -->
![Tokenization](https://media.geeksforgeeks.org/wp-content/uploads/20190301115936/lexical.png)

### Team Members
>+ [Mboh Bless Pearl N](https://www.github.com/MbohBless)
>+ [Seukam Kamadeu Samira](https://github.com/Kamadeusamira)
>+ [Fontem Favour](https://github.com/FONTEM123)

# Classes involved 
**statement_tokenizer**
  * there is an initialization of the class with the regular expressions that would be used to tokenize the text

```
    def __init__(self):
     
        self._pattern = r"[A-Z]+[a-z]*\s\."
        self._sentence_pattern = r'([A-Z][^\.!?]*[\.!?])'
        self._word_pattern = r'\w+'
        self._regex = re.compile(self._sentence_pattern)
        self._tokens = []
```
**tokenize**
  * this method is used to tokenize the text into sentences and words


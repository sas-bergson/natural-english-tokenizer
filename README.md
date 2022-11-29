<<<<<<< HEAD
# natural-english-tokenizer

# --------------- terminologies and structure

# ---------------------------- structure of a compiler

compiler: frontend, optimizer and backend

frontend: scanner, parser and elaborator

optimizer: ...

backend: analysis || translation

# ---------------------------- general structure of sentences

Simple sentence

Compound Sentence

Complex sentence

Compound-Complex sentence

# ---------------------------- types of sentences

Declarative Sentence

Interrogative Sentence

Exclamatory Sentence

Imperative Sentence

# ---------------------------- structure of a sentence

sentence = phrase || clause

sentence += word

sentence = object + predicate || predicate and object

object = object || interjection + conjunction + adverb + preposition + pronoun + adjective + object

predicate = verb + object + endmark || adverb + verb + object + endmark

# ---------------------------- sentence tenses

past sentence tense = past simple || past perfect || past continuous || past perfect continuous

present sentence tense = present simple || present perfect || present continuous || present perfect continuous

future sentence tense = future simple || future perfect || future continuous || future perfect continuous

# ---------------------------- methodology

frontend: tokenization -> lower casing

optimizer: stop words removal -> stemming || lemmatization

backend: analysis || translation

#
=======
# Natural English Tokenizer (NET)

NET (Natural English Tokenizer) is a tool that helps in scanning and parsing text written in natural english in order to prepare them for spell-cheking and grammar checking.

### Wed Nov 27 18:30 modified the tokenizer as a class
 - created scanner module
 - created tokenizer class in order to allow use of tokenizer objects
 - created main.py as driver code 
 
### Wed Nov 19 16:00 initialized the tokenizer repository
 - created default statement.py 
 - created readme file
>>>>>>> 10e424036b434eb39a22770d9db8d3b1c7ba40da

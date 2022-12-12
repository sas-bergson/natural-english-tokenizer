import sys
import re


text = "Its show time"

punctuation = ['!', '?',',','.',';',':']
noun = ['+', '-', '*', '/', '=', '+=', '-=', '==', '<', '>', '<=', '>=']
adverb = ['auto','break', 'case', 'char', 'const', 'continue', 'default', 'do', 
			'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 
			'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 
			'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
verb = [ 'gag' , 'gain' , 'gallop', 'gamble' ,'gargle' ,'garnish' ,'gasp' ,'gather','gauge' ,'geld' ,'generalize' ,'generate' , 'germinate' , 'gesticulate', 
 'get' , 'giggle', 'gild' ,'give', 'glance', 'glaze' ,'gleam' ,'glean' ,'glide' ,'glimmer', 'glimpse' ,'glisten' ,'glitter' ,'glorify', 'gloss' ,'glow' ,'glue' ,'gnash' ,'gnaw' ,'go' ,'goad', 'gossip',  'govern' ,'grab' , 'grace' ,'grade' ,'graduate' 
, 'graft','grant', 'granulate','grasp','grate','gravel','gravitate','graze','grease','greet','grill','grin','grind', 'grip', 'groan','groom','grope','grow','growl','grub','grumble','grunt','guarantee','guard','guess','guide', 'gurgle' ,'gush' ,'gut' ,'guzzle' 
]


in_adverb = []
in_spl_punctuation = []
in_noun = []
in_verb = []
in_identifiers = []
in_constants = []

tokens = []
isStr = False
isWord = False
isCmt = 0
token = ''

for i in text:
	if i == '/':
		isCmt = isCmt+1

	elif isCmt == 2:
		if i == '\n':
			token = ''
			isCmt = 0
	
	elif i == '"' or i == "'":
		if isStr:
			tokens.append(token)
			token = ''
		isStr = not isStr 

	elif isStr:
		token = token+i
    
	elif i in punctuation:
		tokens.append(i)
           
	elif i.isalnum() and not isWord:
		isWord = True
		token = i
    
	elif (i in verb) or (i in noun):
		if token:
			tokens.append(token)
			token = ''
        
		if not (i==' ' or i=='\n' or i=='	'):
			tokens.append(i)

	elif isWord:
		token = token+i


for token in tokens:
	if token in punctuation:
		in_spl_punctuation.append(token)

	elif token in noun:
		in_noun.append(token)

	elif token in adverb:
		in_adverb.append(token)
				
	elif re.search("^[_a-zA-Z][_a-zA-Z0-9]*$",token):
		in_identifiers.append(token)
		
	elif token in verb:
		in_verb.append(token)
		
	else:
		in_constants.append(token)
	
						
print("No of tokens = ", len(tokens))   
print("\nNo. of adverb = ",len(in_adverb))
print(in_adverb);
print("\nNo. of special punctuation = ",len(in_spl_punctuation))
print(in_spl_punctuation);
print("\nNo. of noun = ",len(in_noun))
print(in_noun);
print("\nNo. of identifiers = ",len(in_identifiers))
print(in_identifiers);
print("\nNo. of constants = ",len(in_constants))
print(in_constants);
print("\nNo. of verb = ",len(in_verb))
print(in_verb);
f.close()   
import sys
import random
import re
with open(sys.argv[0], 'r') as file1:
 sentence=file1.read()
special_characters = ['!','"','#','$','%','&','(',')','*','+','/',':',';','<','=','>','@','[','\\',']','^','`','{','|','}','~','\t']

for i in special_characters : 
 sentence = sentence.replace(i, '')
 

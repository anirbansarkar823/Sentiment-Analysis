# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:41:13 2019

refer: https://www.geeksforgeeks.org/spelling-checker-in-python/
from spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled
misspelled = spell.unknown(["cmputr", "watr", "study", "wrte"])

for word in misspelled:
	# Get the one `most likely` answer
	print(spell.correction(word))

	# Get a list of `likely` options
	print(spell.candidates(word))

"""

#please download the below:
#import nltk
#nltk.download('punkt')

import re, itertools
tweet = """ThisIsAwesome in th ebeach Here. This is insan in th insan soooooo happppyyyyy
is my new line getting maintained
"""

#split words
tweet = " ".join(re.findall('[A-Z][^A-Z]*',tweet))
print(tweet)

#standardising words
tweet =  ''.join(''.join(s)[:2] for _,s in itertools.groupby(tweet))
print(tweet)
#to test the working of spelling checker
import spellchecker
spell = spellchecker.SpellChecker()
#find misspelled words
from nltk.tokenize import word_tokenize
tweet_tok = word_tokenize(tweet)
print(tweet_tok)
misspelled = spell.unknown(tweet_tok)
for word in misspelled:
    print(word)
    tweet = re.sub(word, spell.correction(word),tweet)
    
print(tweet)



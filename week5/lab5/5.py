'''
Write a Python program
that matches a string 
that has an "a" followed 
by anything, ending in "b"
'''
import re
def aanythingb(text):
    if(re.search('a.*b$',text)):
        return('Match!')
    else:
        return('No match!')
print(aanythingb('adhb'))#m
print(aanythingb('ab'))#m
print(aanythingb('akanab'))#m
print(aanythingb('collaboration'))#nm



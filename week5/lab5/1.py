'''
Write a Python program that 
matches a string that has an 
"a" followed by zero or more "b"s.
'''

import re
def aandbmatches (text):
    if re.search('a(b*)', text):
        return('Match!')
    else:
        return('No match!')
print(aandbmatches("ababb"))#m
print(aandbmatches("collaboration"))#m
print(aandbmatches("cab"))#m
print(aandbmatches("leon"))#nm
print(aandbmatches("moon"))#nm

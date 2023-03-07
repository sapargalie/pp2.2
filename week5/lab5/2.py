'''
Write a Python program that
matches a string that has an
"a" followed by two to three "b"
'''
import re
def aandbmatches (text):
    if re.search('ab{2,3}', text):
        return('Match!')
    else:
        return('No match!')
print(aandbmatches("a"))#nm
print(aandbmatches("abbb"))#m
print(aandbmatches("abc"))#nm
print(aandbmatches("acc"))#nm
print(aandbmatches("abb"))#m
print(aandbmatches("rainbow"))#nm

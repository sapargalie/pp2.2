#write a Python program to find 
#sequences of lowercase letters 
#joined with a underscore.
import re
def lowercase_underscore(text):
    if re.search('^[a-z]+_[a-z]+$',text):
        return('Match')
    else:
        return('No match!')
print(lowercase_underscore("aaq_cgh"))#m
print(lowercase_underscore("dbh_AGG"))#nm
print(lowercase_underscore("aFAaASfh_ab"))#nm

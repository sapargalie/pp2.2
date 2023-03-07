'''
Write a Python program to split a string at uppercase letters.
'''
import re
example="UpperCaseLettersSplit"
example1="HelloWorldIAmBusy"

x=re.findall('[A-Z][a-z]*',example)
x1=re.findall('[A-Z][a-z]*',example1)

print(*x)
print(*x1)

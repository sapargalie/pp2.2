'''
Write a Python program with builtin 
function to multiply all the numbers in a list
'''
from functools import reduce
list=[1,2,3,4,5]
result=reduce((lambda x,y:x*y),list)
print(result)

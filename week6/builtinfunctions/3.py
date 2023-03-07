'''
Write a Python program with builtin 
function that checks whether a passed
 string is palindrome or not.
'''
def palindrome(x):
    listx=list(x)
    listxr=listx.copy()
    listxr.reverse()
    if(listxr==listx):
        print('string is a palindrome')
    else:
        print('string is not a palindrome')
palindrome('something')
palindrome('abba')

'''
Write a Python program with builtin 
function that accepts a string and calculate 
the number of upper case letters and lower case 
letters
'''
def letters(x):
    upper=0
    lower=0
    for i in x:
        if(i.isupper()):
            upper+=1
        if(i.islower()):
            lower+=1
    print("number of uppercase letters of "+ x +" is "+str(upper))
    print("number of lowercase letters of "+ x +" is "+str(lower))
letters("A Lot Of Different WORDS")
letters("HI, my name is Aruzhan")
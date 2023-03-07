#Write a Python program to count the number of lines in a text file.
import os
f=open('textfile.txt','r')
counter=0
for line in f.readlines():
    counter+=1
f.close()
print('Number of lines in "textfile.txt" is : '+str(counter))

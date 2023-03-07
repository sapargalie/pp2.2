#Write a Python program to list only directories,
#files and all directories, files in a specified path.
import os
path = 'C:\Users\erasyl\Desktop\pp2\git\week6'
print("Only directories: ")
for item in os.listdir(path):
    if (os.path.isdir(os.path.join(path,item))):
        print(item,end=' ')
print('\n')
print("Only files: ")
for item in os.listdir(path):
    if(os.path.isfile(os.path.join(path,item))):
        print(item,end=' ')
print('\n')
print("All directories and files: ")
for item in os.listdir(path):
    print(item,end=' ')

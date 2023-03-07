'''
Write a Python program to test whether a given path exists or not.
If the path exist find the filename and directory portion of the given path.
'''
import os
def path_check_filename(path):
    print(path)
    print('---'*20)
    if(os.access(path,os.F_OK)):
        print("PATH EXISTS!")
        print("Directory portion of the given path: ")
        print(os.path.dirname(path))
        print("Filename of the path is ")
        print(os.path.basename(path))
        
    else:
        print("PATH DOESNT EXIST!")
path_check_filename('C:\Users\erasyl\Desktop\Useful materials')
path_check_filename('C:\Users\erasyl\Desktop\pp2\git\week6\lablabla')
path_check_filename('C:\Users\erasyl\Desktop\pp2\git\week6\dirandfiles')

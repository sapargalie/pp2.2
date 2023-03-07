#Write a Python program to write a list to a file.
disciplines = ['Statistics', 'PP2', 'Global Evo', 'Calculus2', 'Kazakh']
with open('semester2.txt', "w") as f:
        for i in disciplines:
                f.write(i+'\n')
content = open('semester2.txt')
print(content.read())
content.close()
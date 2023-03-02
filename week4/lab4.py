import datetime

x = datetime.datetime.now()

# Write a Python program to subtract five days from current date.

x = datetime.datetime.now()
y = x - datetime.timedelta(days=5)

print(y)

print()
print()
print()

# Write a Python program to print yesterday, today, tomorrow.


print(x - datetime.timedelta(days=1))
print((x - datetime.timedelta(days=1)).strftime("%A"))
print(datetime.datetime.now())
print(x.strftime("%A"))
print(x + datetime.timedelta(days=1))
print((x + datetime.timedelta(days=1)).strftime("%A"))


# Write a Python program to drop microseconds from datetime.

print()
print()
print()


DateWithoutMicro = x.replace(microsecond=0)

print(DateWithoutMicro)


# Write a Python program to calculate two date difference in seconds.


date1_str = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d %H:%M:%S')  #strptime used to convert string to date

date2_str = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")
date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d %H:%M:%S')


differ = (date2 - date1).total_seconds()

#result
print("Date 1:", date1)
print("Date 2:", date2)
print("Difference in seconds:", differ)

import math
# Write a Python program to convert degree to radian.


x = float(input())
y = math.radians(x)
print(y)


# Input degree: 15
# Output radian: 0.261904



# Write a Python program to calculate the area of a trapezoid.


# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5


first_base = int(input())
second_base = int(input())
height = int(input())


# area = float(((first_base + second_base)*height)/2)

# print(area)

# Write a Python program to calculate the area of regular polygon.


n = int(input())

lenght = int(input())

area = (n*(math.pow(lenght, 2)))/(4*(math.tan(math.pi/n)))

print(area)


# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625



# Write a Python program to calculate the area of a parallelogram.


a = int(input())
b = int(input())

print(a*b)

#or

sin = float(input())
print(math.sin(math.radians(sin))*a*b)



# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0



# Create a generator that generates the squares of numbers up to some number N.

def squares_until_n(n):
    for i in range(1, n+1):
        yield i**2   #generator lazy iterator, yield used to return iterator 
    
n = int(input())

for squares in squares_until_n(n):
    print(squares)


# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.



def print_even_num(n):
    for i in range(0, n+1): #from zero to n
        if(i%2==0):
            yield i

    
n = int(input())

for evens in print_even_num(n):
    print(evens)



# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.



def some_iter(n):
    for i in range(0, n+1):
        if(i % 3 == 0 and i % 4 == 0):
            yield i

n = int(input())

for myit in some_iter(n):
    print(myit)



# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input())
b = int(input())

for square in squares(a, b):
    print(square)

# Implement a generator that returns all numbers from (n) down to 0.


def reversive(n):
    for i in range(n, 0, -1):
        yield i 

n = int(input())

for rev in reversive(n):
    print(rev)



import json

with open("sample-variant.json", "r") as read_file:
    data = json.load(read_file)
print(data)
print("""Interface Status
================================================================================""")
print("""DN                                             Description          Speed                      MTU """)
for i, k in data["imdata"][0]['l1PhysIf']["attributes"].items():
    if i == 'dn':
        print(k, end="                          ")
    if i == "speed":
        print(k, end="                                         ")
    if i == "mtu":
        print(k, end="                   ")
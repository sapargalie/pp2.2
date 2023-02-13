a = int(input())
b = int(input())
for x in range(a - (a + 1) % 2, b - b % 2, -2):
    print(x, end = ' ')
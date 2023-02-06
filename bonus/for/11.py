n = int(input())
sum = 0
for x in range(1, n + 1):
    sum += x
for x in range(n - 1):
    sum -= int(input())
print(sum)
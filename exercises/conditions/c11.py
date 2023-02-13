x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
xx = abs(x1 - x2)
yy = abs(y1 - y2)
if xx == 1 and yy == 2 or xx == 2 and yy == 1:
    print('YES')
else:
    print('NO')
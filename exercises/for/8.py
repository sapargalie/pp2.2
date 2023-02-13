n = int(input())
part_fact = 1
part_sum = 0
for x in range(1, n + 1):
    part_fact *= x
    part_sum += part_fact
print(part_sum)
def has_33(list):

    for i in range(0, len(list) - 1):

        if list[i] == 3 and list[i + 1] == 3 :

            return True


    return False

a = [int(s) for s in input().split()]

print(has_33(a))
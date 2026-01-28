def doixung(x):
    for i in range (len(x)//2):
        if x[i] != x[-(i+1)]:
            return False
    return True
a=[int(x) for x in input().split()]
print(doixung(a))
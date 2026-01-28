def fi(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fi(n-1)+fi(n-2)
n=int(input())
print(fi(n))
        
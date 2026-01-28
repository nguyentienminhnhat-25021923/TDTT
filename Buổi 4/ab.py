def tich(n):
    return 1 if n<=1 else n*tich(n-1)
n=int(input())
print(tich(n))

a=list(map(int,input().split()))
b=int(input())
for i in range (len(a)):
    if a[i] == b:
        print(i)
        break
else:
    print("-1")
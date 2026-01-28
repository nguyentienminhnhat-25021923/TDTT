a=list(int(x) for x in input().split())
k=int(input())
c=0
for i in range (len(a)):
    if a[i] == k:
        c+=1
        print(c)
        break
else:
    print(0)
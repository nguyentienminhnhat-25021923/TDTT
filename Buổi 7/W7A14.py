n=int(input())
a=list(map(int,input().split()))
b=len(a)
found= False
for i in range (b):
    if a[i]==7:
        print(i, end= ' ')
        found = True
if not found:
    print("not found")

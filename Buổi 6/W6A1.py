a=list(map(int,input().split()))
b=set()
c=[]
for i in a:
    if i not in b:
        b.add(i)
        c.append(i)
print(c)


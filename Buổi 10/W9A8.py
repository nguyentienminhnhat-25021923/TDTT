a,b=0,0
d=input()
c=str(d)
for i in range(len(d)):
    if d[i]=="U":
        b+=1
    if d[i]=="D":
        b-=1
    if d[i]=="L":
        a-=1
    if d[i]=="R":
        a+=1
print(a,b)
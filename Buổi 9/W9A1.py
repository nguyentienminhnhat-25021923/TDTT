a=list(map(int,input().split()))
b=int(input())
c=0
for i in range(len(a)):
    if a[i]==0:
        c+=1
if (c-1)//2>=b:
    print ("True")
else:
    print ("False")

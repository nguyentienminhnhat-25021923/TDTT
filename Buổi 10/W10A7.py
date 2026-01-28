a=list(map(int,input().split()))
b=int(input())
count=0
for i in range(len(a)):
    if a[i]==0:
        l=(i==0) or (a[i-1]==0)
        r=(i==len(a)-1) or (a[i+1]==0)
        if l and r:
            a[i]=1
            count+=1
if count>=b:
    print("true")
else:
    print("false")
n=int(input())
a=0
if n<=10**6:
    for i in range(1,int(n**0.5)+1 ):
        while n%i == 0:
            n=n//i
            a=a+1
    print (a)        
else:
    print("nhập lại")

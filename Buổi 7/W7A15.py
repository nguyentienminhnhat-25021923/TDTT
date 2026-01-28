n=int(input())
ten=[]
for i in range(n):
    b=input()
    ten.append(b)
for i in range(n):
    if ten[i]=="Nemo":
        if i != n-1:
            print(f'{ten[i-1]} and {ten[i+1]}')
        else:
            print(f'{ten[i-1]} and {ten[0]}')
            
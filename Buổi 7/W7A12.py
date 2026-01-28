import string
b=[]
k=string.ascii_uppercase
for i in range(4):
    a=input().strip()
    c=k[i]
    b.append([a,c])
b.sort()
ketqua=[]
for i in b:
    ketqua.append(i[1])
print(" ".join(ketqua))
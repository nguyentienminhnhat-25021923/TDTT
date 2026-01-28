a=int(input("số con: "))
b=int(input("số chân: "))
c=2*a-b/2
d=b/2-a
if c>=0 and d>=0:
    print(f"{int(c)}, {int(d)}")
else:
    print("nhập lại")

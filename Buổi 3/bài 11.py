a=int(input("nhập số nguyên dương a: "))
b=int(input("nhập số nguyên dương b: "))
c=int(input("nhập số nguyên dương c: "))
if a <=0 or b <= 0 or c <=0:
    print("Không phải tam giác")
elif a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Tam giác đều")
    elif (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
        print("Tam giác cân")
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")
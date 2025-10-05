a=int(input("nhập số nguyên dương a: "))
b=int(input("nhập số nguyên dương b: "))
c=int(input("nhập số nguyên dương c: "))
if a <=0 or b <= 0 or c <=0:
    print("No")
elif a+b>c and a+c>b and b+c>a:
    print("Yes")
else:
    print("No")
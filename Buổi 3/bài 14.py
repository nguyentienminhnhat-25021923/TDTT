#giải pt ax+b=0
a=float(input("nhập số a: "))
b=float(input("nhập số b: "))
if a==0:
    if b == 0:
        print("vô số nghiệm")
    else:
        print("vô nghiệm")
else:
    print(f"{(-b/a):.2f}")
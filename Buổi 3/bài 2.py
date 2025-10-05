a=int(input("nhập số a: "))
b=int(input("nhập số b: "))
print(f"trước khi hoán đổi: a={a}, b={b}")
a, b=b, a
print(f"sau khi hoán đổi: a={a}, b={b}")
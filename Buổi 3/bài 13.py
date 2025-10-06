n=int(input("nhập số điện: "))
if 0<n<50:
    a=n*1500
elif 50<n<100:
    a=50*1500+(n-50)*2000
elif n>100:
    a=50*1500+50*2000+(n-100)*3000
print(f"số tiền điện là {a}")
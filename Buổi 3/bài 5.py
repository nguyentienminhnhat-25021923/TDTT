m=int(input("nhập số m:"))
n=int(input("nhập số n:"))
if m%n==0:
    a=m//n
    print(f"kết quả phép chia {m} cho {n} làm tròn xuống là {a}")
else: 
    a=m//n+1
    print(f"kết quả phép chia {m} cho {n} làm tròn lên là {a}")
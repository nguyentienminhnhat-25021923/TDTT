n=int(input("nhập số n: "))
if n > 1000 or n < 0:
    print("không tính được")
else:
    tong = 0
    for i in range (1, n+1):
        tong+=i
    print(f"tổng của các số nguyên từ 1 đến {n} là {tong}")
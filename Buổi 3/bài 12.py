n=int(input("nhập năm muốn kiểm tra có nhuận không: "))
if n % 400 == 0:
    print("Yes")
elif n % 4 == 0:
    if n % 100 == 0:
        print("No")
    else:
        print("Yes")
else:
    print("No")
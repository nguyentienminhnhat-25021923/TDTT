a = input("Chuỗi a: ")
b = input("Chuỗi b: ")
len_b = len(b)
res = ""
i = 0
while i < len(a):
    if a[i:i+len_b] == b:
        i += len_b
    else:
        res += a[i]
        i += 1
print(f"Kết quả: {res}")
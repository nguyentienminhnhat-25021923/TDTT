n=int(input("nhập số nguyên n: "))
if n < 0:
    a = str(abs(n))
    dao_nguoc=a[::-1] 
    so_dao_nguoc=int("-" + dao_nguoc)
else:
    a = str(n)
    dao_nguoc=a[::-1]
    so_dao_nguoc=int(dao_nguoc)
print(f"số đảo ngược là: {so_dao_nguoc}")

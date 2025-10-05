n=int(input("số cần kiểm tra: "))
def luy_thua_2(n):
    if n<=0:
        return False
    result = (n&(n-1)) == 0
    return result
ket_qua = luy_thua_2(n)
print(ket_qua)

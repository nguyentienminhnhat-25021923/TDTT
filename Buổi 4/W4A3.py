n=int(input(""))
if 0<n<100 :
    tich=1
    for i in range (1, n+1):
        tich= tich*i
    print(tich)
else:
    print("nhap lai")

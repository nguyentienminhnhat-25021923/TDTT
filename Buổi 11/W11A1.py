try:
    a,b=map(int,input().split())
    c=a/b
    print(f"{c:.2f}")
except ZeroDivisionError:
        print("Loi chia khong")

    
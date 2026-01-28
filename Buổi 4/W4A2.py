while True:
    try:
        n=int(input("nhập số nguyên dương n: "))
        if n > 0:
            break
        else:
            print("nhập lại")
    except ValueError:
        print("nhập lại")
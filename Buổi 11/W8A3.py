def shp():
    try:       
        a=int(input())
        xuathien=set()
        b=c=0
        while a!=1 and a not in xuathien:
            xuathien.add(a)
            c=0
            while a>0:
                b=a%10
                a=a//10
                c+=b**2
            a=c
        if a==1:
            print("yes")
        else:
            print("no")
    except ValueError:
        print("nhập lại")
shp()

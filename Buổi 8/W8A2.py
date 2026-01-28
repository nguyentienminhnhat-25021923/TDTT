x,y=map(int,input().split())
if x==y==0:
    print("M là gốc toạ độ")
elif x==0 and y!=0:
    print(f"M nằm trên trục hoành và cách O {y} m")
elif x!=0 and y==0:
    print(f"M nằm trên trục tung và cách O {x} m")
else:
    print(f"M cách O {((x**2+y**2)**0.5):.2f} m")
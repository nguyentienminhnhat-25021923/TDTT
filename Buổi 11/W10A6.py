import math
try:
    a=int(input())
    b=math.sqrt(a)
    print(f"{b:.2f}")
except ValueError:
    print("so am")
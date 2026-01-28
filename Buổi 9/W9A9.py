a,b,c,d,e=map(int,input().split())
L = [a, b, c, d, e]
L.remove(max(L))
L.remove(max(L))
print(max(L))
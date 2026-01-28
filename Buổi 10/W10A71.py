n = int(input())
k = 2* n + 1
m = n + 1
for i in range(1, k + 1):
    c = abs(m - i)
    s = k - 2 * c
    print('. ' * c  + '* '* s + '. ' * c)
            
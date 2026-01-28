class cylinder:
    def __init__(self, r, h):
        self.r=r
        self.h=h
        self.pi=3.14
    def s(self):
        return 2*self.pi*(self.r**2) + 2*self.pi*self.r*self.h
    def v(self):
        return self.pi*(self.r**2)*self.h
a,b=map(float,input().split())
c=cylinder(a,b)
print(f"{c.s():.2f}, {c.v():.2f}")
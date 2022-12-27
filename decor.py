class decor:
    def __init__(self,add):
        self.addres=add
    def __call__(self,x,y):
        self.addres(x,y)
        # s=x+y
        return (x+y)**2

# ob=b()
# ob.de()

# fuc()

@decor
def func(x,y):
    return x+y

res=func(2, 1)
print(res)
# r=A()
# r.hii()
# print(r())



a=[10,20,30,40,50]

def fun(a):
    yield a

b=fun(a)
next(b)


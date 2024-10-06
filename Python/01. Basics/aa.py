def generator(a, b):
    x = a*b 
    yield x
    x *= b
    yield x
    x *= b
    yield x\
    
print("hello")

test = generator(1, 2)
print(next(test))
print(next(test))

def ali():
    x=2

    b=33
    d    =4

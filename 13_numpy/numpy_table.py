import numpy as np

def table(m,n):
    arr = []
    for i in range(1,m+1):
        sub = []
        for j in range(1,n+1):
            sub.append(i*j)
        arr.append(sub)
    return np.array(arr)

def table1(m,n):
    arr = [[i*j for j in range(1,n+1)] for i in range(1,m+1)]
    return np.array(arr)

def test():
    arr = table(4,5)
    #arr = table1(4,5)
    print(arr)
    print(arr.ndim)
    print(arr.shape)
    print(arr *2)

test()
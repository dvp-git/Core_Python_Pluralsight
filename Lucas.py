# The Lucas Series:

"""
Lucas series is similar to Fibonacci series and is an infinite series, Condition
L(n) = L(n-1) + L(n-2) for n > 1
L0 = 2
L1 = 1
2,1,3,4,7,11,.... """


def lucas():
    """ Generates the lucas series"""
    yield 2             # yields 2 at first, first element
    L0 = 2
    L1 = 1
    while True:
        yield L1
        L0,L1 = L1,L0 + L1

for item in lucas():
    print(item)             # Prints until computer runs out of memory
    

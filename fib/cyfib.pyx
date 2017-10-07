
def cyfib(int n):
    cdef:
        double a = 1.0
        double b = 0.0
        int i

    for i in range(n):
        a, b = a+b, a

    return a

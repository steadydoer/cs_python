def exp(g, m):
    return (g(m))

def f1(x):
    return x*x

def f2(x):
    return x*x*x

def g3321(x):
    return x**12


n=5
print(n, exp(f1, n))
print(n, exp(f2, n))
print(n, exp(g3321, n))

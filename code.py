
n = 20
iteration = 6


def f(k):
    if k == 1:
        return n
    return ((f(k - 1) + 1) * f(k - 1)) / 2

def g(k):
    if k == 1:
        return 1
    return g(k - 1) + f(k - 1) - 1


value = g(iteration) / f(iteration)
print(value)




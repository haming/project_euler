def gcdRecr(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcdRecr(a-b, b)
    
def gcdIterate(m, n):
    while n:
        m, n = n, m % n
    return m
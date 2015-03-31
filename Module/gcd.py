def gcd(a, b):
    """Return the greatest common divide of a and b"""
    if a == 0:
        return b
    else:
        return gcd(b%a,a)
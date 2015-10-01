def isPrime(num):
    """Return True if num is prime"""
    if num==0 or num==1:
        return False
    if num<4:
        return True
    if num%2==0:
        return False
    if num<9:
        return True
    if num%3==0:
        return False
    r = int(num**0.5)
    f = 5
    while f<=r:
        if num%f==0:
            return False
        if num%(f+2)==0:
            return False
        f += 6
    return True


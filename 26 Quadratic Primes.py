def f(a, b):
    return lambda n: n*n+a*n+b 

def isPrime(num):
    if num==0 or num==1:
        return False
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def consecutivePrimeNum(func):
    n = 0
    while True:
        if isPrime(abs(func(n))):
            n += 1
        else:
            break
    return n
    
maxN = 0
maxC = None  
for a in range(-1000,1001):
    for b in range(-1000,1001):
        func = f(a,b)
        if consecutivePrimeNum(func)>maxN:
            maxN = consecutivePrimeNum(func)
            maxC = (a, b)
            
print maxC, maxC[0]*maxC[1]
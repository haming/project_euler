def fib():
    f0 = 1
    f1 = 1
    while True:
        yield f0
        f0,f1 = f1,f0+f1
        
fibonacci = fib()
n = fibonacci.next()
sum = 0
while n < 4000000:
    if n%2 == 0:
        sum += n
    n = fibonacci.next()
def fib():
    f0 = 1
    f1 = 1
    while True:
        yield f0
        f0,f1 = f1,f0+f1

fibo = fib()
i = 0
while True:
    i += 1
    num = fibo.next()
    if len(str(num))==1000:
        print i
        break

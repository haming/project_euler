def gen_primes():
    yield 2
    n = 3
    while True:
        for x in range(2, int(n**0.5)+1):
            if n % x == 0:
                break
        else:
            yield n
        n += 2
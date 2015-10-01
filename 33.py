def cancelling(numerator, denominator):
    if numerator%10 == denominator%10:
        yield (numerator/10, denominator/10)
    if numerator%10 == denominator/10:
        yield (numerator/10, denominator%10)
    if numerator/10 == denominator%10:
        yield (numerator%10, denominator/10)
    if numerator/10 == denominator/10:
        yield (numerator%10, denominator%10)

        
                        
for n in range(10,100):
    for m in range(n+1,100):
        c = cancelling(n,m)
        if n%10==0 or m%10==0:
            continue
        for (newN, newD) in c: 
            if newD == 0:
                continue
            if abs(float(n)/m - float(newN)/newD) < 0.0001:
                print '%s/%s, %s/%s' % (n,m,newN,newD)
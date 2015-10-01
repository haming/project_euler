def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
    
print factorial(40)/(factorial(20)*factorial(20))
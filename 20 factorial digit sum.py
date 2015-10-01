bigNum = reduce((lambda x,y:x*y),range(1,101))
print sum([int(n) for n in str(bigNum)])
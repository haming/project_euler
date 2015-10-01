direction = [(1,0),(0,-1),(-1,0),(0,1)]
times = 1

def nextDirect():
    direction = 0
    n = 0
    while True:
        repeat = n/2+1
        for i in range(repeat):
            yield direction
        direction = (direction+1)%4
        n += 1

def position():
    position = (0,0)
    n = nextDirect()
    while True:
        yield position
        direct = direction[n.next()]
        position = (position[0]+direct[0], position[1]+direct[1])


n = 1001
p = position()
total = 0
for i in range(1,n*n+1):
    pos = p.next()
    #print pos
    if abs(pos[0]) == abs(pos[1]):
        total += i
        
print total
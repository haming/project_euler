def rightTriangle(perimeter):
    num = 0
    for a in range(1,perimeter/2):
        for b in range(a, perimeter/2):
            if (a**2+b**2)==(perimeter-a-b)**2:
                #print a,b,perimeter-a-b
                num += 1
    return num
    
maxSolution = 0
maxP = 0
for p in range(1,1001):
    solution = rightTriangle(p)
    if solution > maxSolution:
        #print p
        maxSolution = solution
        maxP = p
print maxP, maxSolution
def specialPythagorean():
    for a in range(1,334):
        for b in range(a,667):
            if a**2+b**2==(1000-a-b)**2:
                print(a,b,1000-a-b)
                return a*b*(1000-a-b)
                
print(specialPythagorean())
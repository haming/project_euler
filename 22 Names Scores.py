rawStr = open('22 names.txt','r').read()
names = rawStr.split(',')
names = [n.strip('"') for n in names]
names.sort()

alphabetic = {chr(i):i-64 for i in range(65,91)}
alphabetivalValue = lambda name: sum(alphabetic[c] for c in name.upper())

total = 0
for i,name in enumerate(names):
    total += (i+1)*alphabetivalValue(name)
print total

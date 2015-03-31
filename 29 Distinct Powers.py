items = []
for a in range(2,101):
    for b in range(2,101):
        items.append(a**b)
print len(set(items))


print len(set([a**b for a in range(2,101) for b in range(2,101)]))
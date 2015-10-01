from collections import Counter

cubic = [n**3 for n in xrange(10000)]

digits = [tuple(sorted(str(n))) for n in cubic]

counter = Counter(digits)
# the 5 cubic number can be found before 10000 cubics
print max(counter.values())
# find out the digit the smallest cube has
index = counter.values().index(5)
findout = counter.keys()[index]
# find out the index of smallest cube
print digits.index(findout)
print cubic[5027]
class Fraction(object):
    def __init__(self, num, deno):
        self.num = num
        self.deno = deno
        
    def getNumerator(self):
        return self.num
        
    def getDenominator(self):
        return self.deno
        
    def __add__(self, num):
        newNum = self.num + num * self.deno
        newDeno = self.deno
        return Fraction(newNum, newDeno)
        
    def reverse(self):
        self.num, self.deno = self.deno, self.num
        
    def __str__(self):
        return '%s/%s' % (self.num, self.deno)
        
def nextNum(fraction):
    temp = fraction+1
    temp.reverse()
    return temp+1
    
count = 0
num = Fraction(1,1)
for i in range(1000):
    num = nextNum(num)
    if len(str(num.getNumerator())) > len(str(num.getDenominator())):
        count += 1
        #print num
        
print count
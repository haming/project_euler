fh = open('42 words.txt')
words = [word[1:-1] for word in fh.read().split(',')]

def wordValue(word):
    return sum(ord(l)-64 for l in word.upper())
    
def triangleNum():
    num = 0
    i = 1
    while True:
        num += i
        yield num
        i += 1

t = triangleNum()
triangleNums = [t.next() for i in range(20)]

#maxWordValue = 0
wordNum = 0
for word in words:
    if wordValue(word) in triangleNums:
        #maxWordValue = wordValue(word)
        wordNum += 1
print wordNum
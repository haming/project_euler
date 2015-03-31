width, height = 11, 11

class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def nextPos(self):
        if self.x+1<=width:
            yield Node(self.x+1,self.y)
        if self.y+1<=height:
            yield Node(self.x,self.y+1)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)
        
numPath = 0
def DFS(start, end, path=[]):
    global numPath
    path = path + [start]
    if start == end:
        numPath += 1
    for new in start.nextPos():
        #print tmpPath,new
        if new not in path:
            newPath = DFS(new, end, path)
            if newPath != None:
                return newPath

def printSolution(path):
    for elt in path:
        print elt,

start = Node(0,0)
end = Node(width, height)
DFS(start, end)
print numPath
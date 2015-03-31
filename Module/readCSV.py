def readCSV(filename, seperator=','):
    fh = open(filename)
    fh.readline()
    data = [line.split(seperator) for line in fh]
    return data
def loadConfig(path):

    file = open(path, 'r')
    configLine = file.readline()

    file.close()
    return configLine.split()

def loadPoints(path):
    points = {}
    index = 0
    with open(path, 'r') as f:
        next(f)
        for line in f:
            row = line.split()
            points[index] = []
            for r in row:
                points[index].append(int(r))
            index += 1
    f.close()
    return points

def readTests(self, path):
    file = open(path, 'r')
    files = []
    for line in file:
        row = line.split()
        files.append(row)
    return files

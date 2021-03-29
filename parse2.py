from datetime import datetime, timedelta
from copy import deepcopy

startTime = datetime.now()

table = [x.split(',') for x in open('out.csv', encoding='utf-8').read().splitlines()]
table.insert(1, [(datetime.strptime(table[1][0], '%Y-%m-%d %H:%M:%S') - timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M:%S')] + ([''] * (len(table[0]) - 1)))
table.append([(datetime.strptime(table[len(table) - 1][0], '%Y-%m-%d %H:%M:%S') + timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M:%S')] + ([''] * (len(table[0]) - 1)))
columns = {x:[] for x in table[0][1:]}
theMaxes = deepcopy(columns)
lines = len(table)
newColumns = {x:[0]*lines for x in table[0][1:]}
newTable = [table[0]] + [[0]*len(table[0]) for _ in range(len(table) - 1)]
wfile = open('outtop.csv', 'w', encoding='utf-8')

for y in range(1, len(table)):
    for x in range(1, len(table[y])):
        columns[table[0][x]].append(int(table[y][x]) if table[y][x] != '' else 0)

for y in columns.keys():
    x = columns[y]
    maxes = []
    theEnd = 0
    while theEnd < len(x):
        streamStart = theEnd
        while streamStart < len(x) and x[streamStart] == 0:
            streamStart += 1

        streamEnd = streamStart
        while streamEnd < len(x) and x[streamEnd] != 0:
            streamEnd += 1

        searchIndex = streamStart
        maxIndex = streamStart
        maxValue = 0
        while searchIndex < streamEnd:
            if x[searchIndex] > maxValue:
                maxValue = x[searchIndex]
                maxIndex = searchIndex

            searchIndex += 1

        if maxIndex < len(x):
            maxes.append(maxIndex)

        theEnd = streamEnd

    theMaxes[y] = maxes

for y in theMaxes.keys():
    x = theMaxes[y]
    for z in x:
        newColumns[y][z] = columns[y][z]

for y in range(1, len(table)):
    newTable[y][0] = table[y][0]
    for x in range(1, len(table[y])):
        if newColumns[table[0][x]][y - 1] != 0:
            newTable[y][x] = newColumns[table[0][x]][y - 1]

        else:
            newTable[y][x] = ''

for y in range(len(newTable) - 1, 0, -1):
    if all(v == '' for v in newTable[y][1:]):
        del newTable[y]

for x in newTable:
#    print(*x, sep=',')
    wfile.write(','.join(str(y) for y in x) + '\n')

print('took: ' + str(datetime.now() - startTime))
from datetime import datetime, timedelta
from copy import deepcopy
from pprint import pprint
table = [x.split(',') for x in open('out.csv', encoding='utf-8').read().splitlines()]
table.insert(1, [(datetime.strptime(table[1][0], '%Y-%m-%d %H:%M:%S') - timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M:%S')] + ([''] * (len(table[0]) - 1)))
table.append([(datetime.strptime(table[len(table) - 1][0], '%Y-%m-%d %H:%M:%S') + timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M:%S')] + ([''] * (len(table[0]) - 1)))
columns = {x:[] for x in table[0][1:]}
theMaxes = deepcopy(columns)
lines = len(table)
newColumns = {x:[0]*lines for x in table[0][1:]}
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
print(newColumns)
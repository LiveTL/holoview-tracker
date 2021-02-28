from datetime import datetime, timedelta
from pprint import pprint
table = [x.split(',') for x in open('out.csv', encoding='utf-8').read().splitlines()]
table.insert(1, [(datetime.strptime(table[1][0], '%Y-%m-%d %H:%M:%S') - timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M:%S')] + ([''] * (len(table[0]) - 1)))
table.append([(datetime.strptime(table[len(table) - 1][0], '%Y-%m-%d %H:%M:%S') + timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M:%S')] + ([''] * (len(table[0]) - 1)))
columns = {x:[] for x in table[0][1:]}
for y in range(1, len(table)):
    for x in range(1, len(table[y])):
        columns[table[0][x]].append((table[y][0], int(table[y][x]) if table[y][x] != '' else 0))
for y in columns.keys():
    x = columns[y]
    maxes = []
    theEnd = 0
    while theEnd < len(x):
        streamStart = theEnd
        while streamStart < len(x) and x[streamStart][1] == 0:
            streamStart += 1
        streamEnd = streamStart
        while streamEnd < len(x) and x[streamEnd][1] != 0:
            streamEnd += 1
        searchIndex = streamStart
        maxIndex = streamStart
        maxValue = 0
        while searchIndex < streamEnd:
            if x[searchIndex][1] > maxValue:
                maxValue = x[searchIndex][1]
                maxIndex = searchIndex
            searchIndex += 1
        if maxIndex < len(x):
            maxes.append(maxIndex)
        theEnd = streamEnd
    print(maxes)
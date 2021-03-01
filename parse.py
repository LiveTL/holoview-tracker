from datetime import datetime
startTime = datetime.now()
f = [eval(x) for x in open('out.txt', encoding='utf-8').read().splitlines()[1:]]
nameDict = {x[1]:x[0] for y in f for x in y[1]}
wfile = open('out.csv', 'w', encoding='utf-8')
print('Timestamp', *nameDict.values(), sep=',')
wfile.write('Timestamp' + ',' + ','.join(nameDict.values()) + '\n')
for x in f:
    line = x[0]
    thisLineDict = {z[1]:z[2] for z in x[1]}
    thisLineList = []
    for x in nameDict.keys():
        if x in thisLineDict:
            if thisLineDict[x] != None:
                thisLineList += [str(thisLineDict[x])]
            else:
                thisLineList += ['']
        else:
            thisLineList += ['']
    print(line, *thisLineList, sep=',')
    wfile.write(line + ',' + ','.join(thisLineList) + '\n')
print('took: ' + str(datetime.now() - startTime))
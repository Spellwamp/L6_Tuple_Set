tuples = ('asdweh', 'ouyuqnv', 'zasbvry')
finaly = []
for i in range(len(tuples)):
    for j in range(len(tuples[i])):
        if tuples[i][j] in 'aeiouy':
            finaly.append(tuples[i][j])
            # print(tuples[i][j], end='')
        else: print(tuples[i][j], end=' ')
finaly = tuple(finaly)
print()
for i in range(len(finaly)):
    print(finaly[i], end=' ')

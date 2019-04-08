tuples = (1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 7, 1, 2, 'q', 'w', 'e', 'r', 'S', 'R', 'S', 'q')
number = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set_n = []
a = []
A = []
for i in range(len(tuples)):
    if type(tuples[i]) == int:
        set_n.append(tuples[i])
    elif 96 < ord(tuples[i]) < 123:
        if tuples[i] not in a:
            a.append(tuples[i])
    elif 64 < ord(tuples[i]) < 91:
        if tuples[i] not in A:
            A.append(tuples[i])
a.sort()
A.sort()
print(a, A, number - set(set_n))

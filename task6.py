"""
Задано n рядочків символів. Розробити програму, яка визначає і друкує окремо
приголосні та голосні малі літери латинського алфавіту, які є в кожному рядку.
"""
tuples = ('asdweh', 'ouyuqnv', 'zasbvry')
final = []
for i in range(len(tuples)):
    for j in range(len(tuples[i])):
        if tuples[i][j] in 'aeiouy':
            final.append(tuples[i][j])
            # print(tuples[i][j], end='')
        else: print(tuples[i][j], end=' ')
final = tuple(final)
print()
for i in range(len(final)):
    print(final[i], end=' ')

# final = []
# for i in range(len(tuples)):
#     for j in range(len(tuples[i])):
#         if tuples[i][j] in 'aeiouy':
#             final.append(tuples[i][j])
#             continue
#            print(tuples[i][j], end='')
        # print(tuples[i][j], end=' ')
# final = tuple(final)
# print()
# for i in range(len(final)):
#     print(final[i], end=' ')

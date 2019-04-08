"""
відобразити реверс одного з кортежів.
"""
new_l = (123, 2, 1, 'a', 's', 's', ',')

o = -1
for i in range(len(new_l)):
    print(new_l[o], end=' ')
    o -= 1
# new_l = list(new_l)
# new_l.reverse()
# print(new_l)

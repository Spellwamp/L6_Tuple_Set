"""
розділити список на декілька, кожний з яких містить тільки
цифри, тільки літери тощо;
"""
new_l = [123, 2, 1, 'ad', 'asd', 'asd', '|\|']
l_w = []
l_n = []
l_e = []

for i in new_l:
    if type(i) == int:
        l_n.append(i)
    elif ord(i[0]) > 64 and ord(i[0]) < 91 or ord(i[0]) > 96 and ord(i[0]) < 123:
        l_w.append(i)
    else: l_e.append(i)

print(l_w, l_n, l_e, end='\n')

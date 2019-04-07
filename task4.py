new_l = ('1', '2', '1', 'a', 's', 's', ',')
new_t = []
for i in range(len(new_l)):
    new_t.append(ord(new_l[i]))
a, b, c = str(input()), str(input()), str(input())
a = new_t.index(ord(a))
b = new_t.index(ord(b))
c = new_t.index(ord(c))

print(a, b, c)

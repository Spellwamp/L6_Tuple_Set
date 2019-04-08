"""
ввести з клавіатури почергово цифру, літеру чи спецсимвол і
повернути відповідно індекс входження у відповідний кортеж;
"""

new_l = ('1', '2', '1', 'a', 's', 's', ',')
new_t = []
for i in range(len(new_l)):
    new_t.append(new_l[i])
a, b, c = input(), input(), input()
a = new_t.index(a)
b = new_t.index(b)
c = new_t.index(c)

print(a, b, c)

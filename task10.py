"""
Задано два символьних рядка із малих і великих латинських літер та цифр.

Розробити програму, яка будує і друкує в алфавітному порядку множину літер, які є
в обох масивах, і множини літер окремо першого і другого масивів.
"""

my_list = ('a', 's', 'b', 'b', '2', 'A', '1')
my_list2 = ('z', 's', 'd', '2', '3', 'h', 'A')
res_1 = set()
res_2 = set()

for i in range(len(my_list)):
    if my_list[i] in my_list2 and not 47 < ord(my_list[i]) < 58:
        res_1.add(my_list[i])
    elif my_list[i] not in my_list2 and not 47 < ord(my_list[i]) < 58: res_2.add(my_list[i])
res_l = sorted(res_1)
res_l_2 = sorted(res_2)
print(res_l, res_l_2)

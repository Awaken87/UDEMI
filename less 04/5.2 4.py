"""
Дан список из 10 элементов. Найти максимальный элемент списка и
переместить его в начало списка.
"""

l = [20, -5, -7, -3, -8, 4, 9, -1, 5, 7]
max_i = max(l)
if max_i == l[0]:
    print(l)
else:
    l.insert(0, max_i)
    print(l)
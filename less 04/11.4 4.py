"""
Дано логическое выражение ¬А ˄ (С ˅ А) ˄ (В ˅ ¬С).
Укажите значения логических переменных A, B и С, при которых значение выражения будет ложным.

a   b   c   not a   c or a      b or not c      f
0   0   0   1       0           1               0
0   0   1   1       1           0               0
0   1   0   1       0           1               0
0   1   1   1       1           1               1       +
1   0   0   0       1           1               0
1   0   1   0       1           0               0
1   1   0   0       1           1               0
1   1   1   0       1           1               0
"""

a = 0
b = 1
c = 1

f = not a and (c or a) and (b or not c)
print(f)
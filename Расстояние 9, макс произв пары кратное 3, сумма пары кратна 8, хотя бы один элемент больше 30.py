#Расстояние 9, произведение пары максимально и кратно 3, сумма кратна 8
#один элемент пары больше 30
n = int(input())
line = []
m = [-10000000]*8
m30 = [-10000000]*8
m3 = [-10000000]*8
m3_30 = [-10000000]*8
max = 0
a = 0
b = 0
for i in range(8):
    x = int(input())
    line.append(x)
for i in range(8, n):
    x = int(input())
    ost = x % 8
    dop = (8 - ost) % 8
    if (x % 3 == 0) and (x > 30) and (x * m[dop] > max):
        max = x * m[dop]
        a = m[dop]
        b = x
    if (x % 3 == 0) and (x < 30) and (x * m30[dop] > max):
        max = x * m30[dop]
        a = m30[dop]
        b = x
    if (x % 3 != 0) and (x > 30):
        if (x * m3[dop] > max):
            max = x * m3[dop]
            a = m3[dop]
            b = x
        if (x * m3_30[dop]>max):
            max = x * m3_30[dop]
            a = m3_30[dop]
            b = x
    if (x % 3 != 0) and (x < 30)and (x * m3_30[dop] > max):
        max = x * m3_30[dop]
        a = m3_30[dop]
        b = x
    trash = line[i%8]
    ost = line[i%8]%8
    if (trash % 3 == 0) and (trash > 30) and (trash > m3_30[ost]):
        m3_30[ost]=trash
    if (trash % 3 == 0) and (trash < 30) and (trash > m3[ost]):
        m3[ost]=trash
    if (trash % 3 != 0) and (trash > 30) and (trash > m30[ost]):
        m30[ost]=trash
    if (trash % 3 != 0) and (trash < 30) and (trash > m3[ost]):
        m[ost]=trash
    line[i%8] = x
print(a, b, max)
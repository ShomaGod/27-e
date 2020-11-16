m = [-10000000]*8
m20 = [-10000000]*8
max = -1000000
line = [0]*3
n = int(input())
for i in range(3):
    x = int(input())
    line[i]=x
for i in range(3,n):
    x = int(input())
    ost = x % 8
    dop = (8-ost)%8
    if (x > 20):
        if (x * m[dop] > max):
            max = x * m[dop]
        if (x * m20[dop] > max):
            max = x * m20[dop]
    if (x < 20):
        if (x * m20[dop] > max):
            max = x * m20[dop]
    ost = line[i%3]%8
    trash = line[i%3]
    if (trash > 20):
        if trash > m20[ost]:
            m20[ost]=trash
    if (trash < 20):
        if trash > m[ost]:
            m[ost]=trash
    line[i%3] = x
print(max)

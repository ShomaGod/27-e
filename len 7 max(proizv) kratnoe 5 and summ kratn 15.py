m = [1000000000]*15
m5 = [1000000000]*15
min = 10000000
line = [0]*7
n = int(input())
for i in range(7):
    x=(int(input()))
    line[i] = x
for i in range(7,n):
    x = int(input())
    ost = x % 15
    dop = (15-ost)%15
    if (x % 5 == 0):
        if (x * m[dop] < min):
            min = x * m[dop]
        if (x * m5[dop]< min):
            min = x * m5[dop]
    if (x % 5 != 0):
        if (x * m5[dop] < min):
            min = x * m5[dop]
    ost = line[i%7]%15
    trash = line[i%7]
    if (trash % 5 == 0):
        if trash < m5[ost]:
            m5[ost]=trash
    if (trash % 5 != 0):
        if trash < m[ost]:
            m[ost]=trash
    line[i%7] = x
print(min)

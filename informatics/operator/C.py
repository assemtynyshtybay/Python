a = int(input())
b = int(input())
c = str(a)+str(b)
v = 0
for i in range(len(c)):
    if c[i] == c[len(c)-i-1]:
        v = v + 1
if v > 0:
    print('YES')
else:
    print('NO')
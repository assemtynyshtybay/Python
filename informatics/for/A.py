a = int(input())
b = int(input())
s = ''
for i in range(a, b+1):
    if i%2 == 0:
        s = s + str(i) + ' '
    else:
        continue
print(s)
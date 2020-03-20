import math
a = int(input())
b = int(input())
s = ''
for i in range(a, b+1):
    if int(math.sqrt(i))*int(math.sqrt(i)) == i:
        s = s + str(i)+' '
print(s)
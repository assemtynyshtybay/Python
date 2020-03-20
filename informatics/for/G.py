s = int(input())
# for i in range(s+1):
#     if s % i == 0:
#         print(i)
i = 2
while s % i != 0:
    i += 1
print(i)
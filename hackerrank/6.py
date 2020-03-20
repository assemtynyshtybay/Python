# Leap year
# def is_leap(year):
#     leap = False
#     if  year%400==0:
#         leap=True
#     elif year%100 ==0:
#         leap=False
#     elif year%4==0:
#         leap=True
#     return leap
# year = int(input())
# print(is_leap(year))
#initial matrix
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list = []

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    list.append([i,j,k])
    print(list)
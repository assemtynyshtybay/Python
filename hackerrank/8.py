if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mx = -100
    mx2 = -100
    for i in arr:
        if i > mx:
            mx2= mx
            mx = i
        elif i > mx2 and i != mx:
            mx2 = i
    print(mx2)
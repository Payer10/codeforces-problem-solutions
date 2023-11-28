n, t = map(int, input().split())
if t == 10:
    if n == 1:
        print(-1)
        exit()
    else:
        print('1' + '0' * (n-1))
        exit()
else:
    num = str(t) + '0' * (n-1)
    print(num)

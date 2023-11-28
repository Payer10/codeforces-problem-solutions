from math import lcm
for i in range(int(input())):
    n ,x ,y = map(int,input().split())
    u = n // x - n // lcm(x,y)
    v = n // y - n // lcm(x,y)
    print(n * (n + 1) // 2 - (n - u) * (n - u + 1) // 2 - v * (v + 1) // 2)
    
n = int(input())
c =p=0
for _ in range(n):
    s = input()
    c+= s!=p
    p=s
print(c)

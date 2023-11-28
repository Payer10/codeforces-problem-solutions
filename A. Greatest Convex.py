def Greatest_Convex(n):
    if(n==0):
        return -1
    return n-1
for i in range(int(input())):
    n=int(input())
    print(Greatest_Convex(n))

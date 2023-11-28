import math
def solve(Number):
    li=0
    for j in range(1,int(Number**.33)+1):
        va=j
        for a in range(1,int(Number**.33)+1):
            a=va**3+a**3
            if(a==Number):
                li+=1
                break
    if(li>0):
        return True
    return False
if __name__ == "__main__":
    for i in range(int(input())):
        Number=int(input())
        if(solve(Number)):
            print('YES')
        else:
            print('NO')

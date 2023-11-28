for i in range(int(input())):
    Num=int(input())
    li=list(map(int,input().split()))
    s=''.join(map(str,li))
    print(s.strip('0').count('0'))

for i in range(int(input())):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    s=(a,b,c,d)
    if(max(s)==d and min(s)==a or min(s)==d and max(s)==a):
        print('YES')
    elif(max(s)==b and min(s)==c or max(s)==c and min(s)==b):
        print('YES')
    else:
        print('NO')

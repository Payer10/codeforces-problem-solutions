for i in range(int(input())):
    a,b=map(int,input().split())
    s,c=abs(a),abs(b)
    if(s==c):
        print(2*s)
    else:
        print(2*max(s,c) - 1)
        

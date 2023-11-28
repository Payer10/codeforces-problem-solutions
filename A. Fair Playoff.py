for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    if(max(a,b)<c and max(a,b)<d):
        print("NO")
    elif(max(c,d)<a and max(c,d)<b):
        print("NO")
    else:
        print("YES")
            

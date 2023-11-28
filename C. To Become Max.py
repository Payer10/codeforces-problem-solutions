for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if(abs(k-max(a))<=1):
        print(max(max(a),k)+1)
    elif(k>=max(a)):
        print(max(a)+1)
    else:
        print(max(a))
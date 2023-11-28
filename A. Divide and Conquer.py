from math import floor
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if(sum(l)%2==0):
        print(0)
    else:
        odd,even=[],[]
        for i in range(n):
            if(l[i]%2==1):
                odd.append(l[i])
            else:
                even.append(l[i])
        a=min(odd)
        b=0
        for i in range(a*2):
            if(a==0):
                break
            else:
                a=a//2
                b+=1
        if(len(even)>0):
            c=min(even)
            d=0
            for i in range(c*2):
                if(c==1):
                    break
                else:
                    c=c//2
                    d+=1
        if(len(even)==0 or min(odd)<min(even)):
            print(b)
        else:
            print(min(b,d))







        

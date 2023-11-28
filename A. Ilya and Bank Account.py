n=int(input())
if(n>=0):
    print(n)
else:
    div1 = n%10
    s1 = (n//10)+1
    div2 = s1%10
    s2 = (s1-div2)+div1
    if(s1%10==0 or s1>=s2):
        print(s1)
    else:
        print(s2)
    

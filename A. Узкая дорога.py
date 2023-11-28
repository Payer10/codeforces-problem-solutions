n=int(input())
li=[]
for i in range(1,n+1):
    a=int(input())
    li.append(a-i)
    n=set(li)
    print(len(n))

    

t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    li=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    large=0
    for i in s:
        if(li.index(i)>large):
            large=li.index(i)
    print(large+1)

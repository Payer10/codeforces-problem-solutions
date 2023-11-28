def Eating_Candies(n,li):
    l=0
    r=n-1
    suml=li[0]
    sumr=li[n-1]
    ans=0
    while l<r:
        if sumr==suml:
            ans=max(ans,1+l+n-r)
        if suml<=sumr:
            l+=1
            suml+=li[l]
        elif suml>sumr:
            r-=1
            sumr+=li[r]
    return ans
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))           
    print(Eating_Candies(n,l))            

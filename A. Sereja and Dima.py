Number=int(input())
a=list(map(int,input().split()))
for f in range(Number):
    i=0
    j=0
    max=0
    k=0
    play1=0
    play2=0
    while(i<=j):
        if(a[i]>=a[j]):
            max=a[i]
            i+=1
        else:
            max=a[j]
            j+=1
        if(k%2==0):
            play1+=max
        else:
            play2+=max
    k+=1
print(play1,play2)
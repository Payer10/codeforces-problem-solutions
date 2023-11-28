def divisible(n):
    ans=0
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if int(n[i]+n[j]) % 25 == 0:
                ans=len(n)-i-2
    return(ans)
for _ in range(int(input())):
    n=input()
    print(divisible(n))
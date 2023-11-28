def Distinct_split(n,s):
    a=len(set(s))
    li=[]
    for i in range(n):
        if s[i] not in li:
            a=max(a,len(set(s[:i+1]))+len(set(s[i+1:])))
            li.append(s[i])
    return a
for i in range(int(input())):
    n=int(input())
    s=input()
    print(Distinct_split(n,s))

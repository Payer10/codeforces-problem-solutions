Number=int(input())
s=list(map(int,input().split()))
a=s[::-1].index(min(s))
b=s.index(max(s))
if((a+b)>=Number):
   print(a+b-1)
else:
    print(a+b)

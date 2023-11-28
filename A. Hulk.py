n=int(input())
x=""
for i in range(1,n):
    if(i%2==1):
        x+="I hate that "
    else:
        x+="I love that "
if(n%2==1):
    x+="I hate it"
    print(x)
else:
    x+="I love it"
    print(x)
    

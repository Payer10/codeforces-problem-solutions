Number,digit=map(int,input().split())
for i in range(digit):
    lastdigit=int(repr(Number)[-1])
    if(lastdigit==0):
        Number=Number//10
    else:
        Number=Number-1
print(Number)

Number=int(input())
if(Number<3):
    print(Number)
else:
    count=0
    for i in range(1,Number+1):
        count+=(Number*i)
    print(count-Number)

Number=int(input())
rest=Number//2
var=Number-rest
for i in range(Number):
    if((rest%2==0 and var%3==0)or(rest%3==0 and var%2==0)or(rest%2==0 and var%5==0)or(rest%3==0 and var%5==0)or(rest%2==0 and var%7==0)or(rest%3==0 and var%7==0)and(rest%5==0 and var%7==0)):
        print(rest,var)
        break
    else:
        rest-=1
        var+=1
    






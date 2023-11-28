Number = int(input())
for i in range(Number):
    str_Num = input()
    new_Num = str_Num[:3]
    rest_Num = str_Num[3:]
    countNum = (int(new_Num[0])+int(new_Num[1])+int(new_Num[2]))
    sumNum = (int(rest_Num[0])+int(rest_Num[1])+int(rest_Num[2]))
    if(countNum == sumNum):
        print("YES")
    else:
        print("NO")

testNum,inputNum=map(int,input().split())
sumcolor=""
for i in range(testNum):
    colorName=str(input().split())
    sumcolor+=colorName
if("C" in sumcolor or "M" in sumcolor or "Y" in sumcolor):
    print("#Color")
elif("W" in sumcolor or "B" in sumcolor or "G" in sumcolor):
    print("#Black&White")

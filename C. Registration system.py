testCases=int(input())
inputedStrs={}
for i in range(testCases):
    string=input()
    if(string in inputedStrs):
        print(string+str(inputedStrs[string]))
        inputedStrs[string] += 1
    else:
        print("OK")
        inputedStrs[string]=1

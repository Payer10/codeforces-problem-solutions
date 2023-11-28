for i in range(int(input())):
    Number=int(input())
    string=input()
    newstr="Timur"
    sortnew=sorted(newstr)
    sortstr=sorted(string)
    if(sortnew==sortstr):
        print("YES")
    else:
        print("NO")

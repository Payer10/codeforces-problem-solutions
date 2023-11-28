for i in range(int(input())):
    string=input()
    newstr=""
    for i in range(len(string)):
        newstr+=string[i]
        if(string[i]==string[i+1]):
            string.remove(string[i])
        else:
            newstr+=string[i]
    print(newstr)

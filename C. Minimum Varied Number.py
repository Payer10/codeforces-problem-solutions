for i in range(int(input())):
    Number=int(input())
    newli=''
    for a in range(9):
        b=9-a
        if(Number>=b):
            Number=Number-b
            newli+=str(b)
            if(Number==0):
                break
    l=''.join(sorted(newli, key=str.lower))
    print(l)
            

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    e=l[0]
    for i in l:
        if e<=i and c==0:
            print(1,end='')
            e=i
        elif e<=i and i<=l[0]:
            print(1,end='')
            e=i
        else:
            if i<=e and i<=l[0] and c==0:
                c+=1
                e=i
                print(1,end='')
            else:
                print(0,end='')
    print()
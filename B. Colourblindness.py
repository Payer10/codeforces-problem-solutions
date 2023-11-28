for _ in range(int(input())):
    Number=int(input())
    frist=input()
    second=input()
    for i in range(Number):
        if(frist[i]=='R' and second[i]=='G' or frist[i]=='R' and second[i]=='B' or frist[i]=='B' and second[i]=='R' or frist[i]=='G' and second[i]=='R'):
            print('No')
            break
    else:
        print('Yes')

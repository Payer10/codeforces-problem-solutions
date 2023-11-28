for _ in range(int(input())):
    n=input()
    a=str(int(n[-2])+int(n[-1]))
    print(n[0:len(n)-2]+a)

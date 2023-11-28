for i in range(int(input())):
    s=input()
    l=len(s)
    st=''
    for i in s:
        if i in st:
            l-=2
            st=''
        else:
            st+=i
    print(l)

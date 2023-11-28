for i in range(int(input())):
    xa,ya=map(int,input().split())
    xb,yb=map(int,input().split())
    xc,yc=map(int,input().split())
    ab=abs(xa-xb)+abs(ya-yb)
    ac=abs(xa-xc)+abs(ya-yc)
    bc=abs(xb-xc)+abs(yb-yc)
    print((ab-bc+ac)//2 +1)
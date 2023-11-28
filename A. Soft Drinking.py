n,k,l,c,d,p,nl,np=map(int,input().split())
kl=(k*l)//nl
cd=c*d
pnp=p//np
restNum=min(kl,cd,pnp)
print(restNum//n)

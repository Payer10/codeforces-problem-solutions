h=0
for i in range(int(input())):
    a=input()
    if(a=="Tetrahedron"):
        h+=4
    elif(a=="Cube"):
        h+=6
    elif(a=="Octahedron"):
        h+=8
    elif(a=="Dodecahedron"):
        h+=12
    elif(a=="Icosahedron"):
        h+=20
print(h)
        

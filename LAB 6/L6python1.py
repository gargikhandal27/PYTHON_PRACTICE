'''i = 1
while i<=9:
    j=1
    while j<=9:
        print(f"{i*j:2d}",end=" ")
        j=j+1
    print()
    i=i+1'''
        
for i in range (1,10):
    for j in range (1,10):
        print(i*j,end=" ")
    print()